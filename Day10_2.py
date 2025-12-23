import re
from z3 import *

def solve_machine(line):
    # 1. Parse the input line
    # Regex to find button wirings (...) and joltage targets {...}
    button_groups = re.findall(r'\(([\d,]+)\)', line)
    target_group = re.search(r'\{([\d,]+)\}', line)
    
    if not button_groups or not target_group:
        return 0

    # Parse targets
    targets = [int(x) for x in target_group.group(1).split(',')]
    num_counters = len(targets)
    
    # Parse buttons into vectors
    # Each button is a vector of 0s and 1s of length num_counters
    buttons = []
    for b_str in button_groups:
        indices = [int(x) for x in b_str.split(',')]
        vec = [0] * num_counters
        for idx in indices:
            if idx < num_counters:
                vec[idx] = 1
        buttons.append(vec)

    # 2. Set up Z3 Solver
    opt = Optimize()
    
    # Create integer variables for each button press count
    # x_0, x_1, ... correspond to the number of times we press button 0, button 1, etc.
    press_vars = [Int(f'b_{i}') for i in range(len(buttons))]
    
    # Constraint 1: Presses must be non-negative
    for v in press_vars:
        opt.add(v >= 0)
        
    # Constraint 2: The sum of button effects must equal the target for each counter
    # For each counter 'c' (joltage slot):
    # Sum(press_count_b * button_b_effect_on_c) == target_c
    for c in range(num_counters):
        opt.add(Sum([press_vars[b] * buttons[b][c] for b in range(len(buttons))]) == targets[c])
        
    # Objective: Minimize the total number of presses
    total_presses = Sum(press_vars)
    opt.minimize(total_presses)
    
    # 3. Solve
    if opt.check() == sat:
        model = opt.model()
        return model.eval(total_presses).as_long()
    else:
        print(f"No solution found for machine: {line[:20]}...")
        return 0

def main():
    # Read input from file
    try:
        with open('input10.txt', 'r') as f:
            data = f.read().strip().splitlines()
    except FileNotFoundError:
        print("Please ensure 'input.txt' exists with your puzzle input.")
        return

    total_presses = 0
    
    print("Calculating...")
    for line in data:
        if line.strip():
            result = solve_machine(line)
            total_presses += result
            
    print(f"Total minimal button presses required: {total_presses}")

if __name__ == "__main__":
    main()