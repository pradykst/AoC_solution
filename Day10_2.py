import re
from z3 import *

def solve_machine(line):
                             
                                                                  
    button_groups = re.findall(r'\(([\d,]+)\)', line)
    target_group = re.search(r'\{([\d,]+)\}', line)
    
    if not button_groups or not target_group:
        return 0

                   
    targets = [int(x) for x in target_group.group(1).split(',')]
    num_counters = len(targets)
    
                                
                                                                 
    buttons = []
    for b_str in button_groups:
        indices = [int(x) for x in b_str.split(',')]
        vec = [0] * num_counters
        for idx in indices:
            if idx < num_counters:
                vec[idx] = 1
        buttons.append(vec)

                         
    opt = Optimize()
    
                                                          
                                                                                       
    press_vars = [Int(f'b_{i}') for i in range(len(buttons))]
    
                                                
    for v in press_vars:
        opt.add(v >= 0)
        
                                                                                    
                                          
                                                           
    for c in range(num_counters):
        opt.add(Sum([press_vars[b] * buttons[b][c] for b in range(len(buttons))]) == targets[c])
        
                                                     
    total_presses = Sum(press_vars)
    opt.minimize(total_presses)
    
              
    if opt.check() == sat:
        model = opt.model()
        return model.eval(total_presses).as_long()
    else:
        print(f"No solution found for machine: {line[:20]}...")
        return 0

def main():
                          
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