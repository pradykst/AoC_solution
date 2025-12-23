from collections import deque
import re

                     
PATTERN_RE = re.compile(r'\[([.#]+)\]')
BUTTONS_RE = re.compile(r'\(([^)]*)\)')

def parse_line(line: str):
    """
    Parse one machine line:
      [.##.] (3) (1,3) ... {ignored}
    Returns: (n_lights, target_mask, button_masks_list)
    """
                                      
    if "{" in line:
        line = line.split("{", 1)[0]
    line = line.strip()

                
    m = PATTERN_RE.search(line)
    if not m:
        raise ValueError(f"No pattern found in line: {line}")
    pattern = m.group(1)
    n = len(pattern)

                                       
    target_mask = 0
    for i, ch in enumerate(pattern):
        if ch == "#":
            target_mask |= (1 << i)

                
    buttons = []
    for group in BUTTONS_RE.findall(line):
        group = group.strip()
        if not group:
            continue
        indices = [int(x.strip()) for x in group.split(",") if x.strip()]
        mask = 0
        for idx in indices:
            if not (0 <= idx < n):
                raise ValueError(f"Button index {idx} out of range for n={n}")
            mask |= (1 << idx)
        buttons.append(mask)

    return n, target_mask, buttons

def min_presses(n: int, target_mask: int, buttons):
    """
    BFS over all 2^n light configurations.
    Each edge = press one button (XOR with its mask).
    Return minimum number of presses to reach target_mask from 0.
    """
    if target_mask == 0:
        return 0                   

    max_state = 1 << n
    dist = [-1] * max_state
    q = deque()

    start = 0
    dist[start] = 0
    q.append(start)

    while q:
        state = q.popleft()
        d = dist[state]

        if state == target_mask:
            return d

        for mask in buttons:
            nxt = state ^ mask
            if dist[nxt] == -1:
                dist[nxt] = d + 1
                q.append(nxt)

                                                         
    return None

def solve(path: str = "input10.txt") -> int:
    total_presses = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            n, target_mask, buttons = parse_line(line)
            presses = min_presses(n, target_mask, buttons)
            if presses is None:
                                                                           
                raise ValueError(f"Machine unsolvable for line: {line}")
            total_presses += presses

    return total_presses

if __name__ == "__main__":
    print(solve("input10.txt"))                             
