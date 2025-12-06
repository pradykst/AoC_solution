def parse_grid(path):
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    
    lines = [ln for ln in lines if ln is not None]
    width = max(len(ln) for ln in lines) if lines else 0

    padded = [ln.ljust(width) for ln in lines]

    return padded

def find_problem_segments(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    is_blank_col = []
    for c in range(cols):
        blank = True
        for r in range(rows):
            if grid[r][c] != " ":   
                blank = False
                break
        is_blank_col.append(blank)

    segments = []
    c = 0
    while c < cols:
        if is_blank_col[c]:
            c += 1
            continue

        start = c
        while c < cols and not is_blank_col[c]:
            c += 1
        end = c - 1

        segments.append((start, end))

    return segments

def eval_problem_columnwise(grid,start,end):
    rows=len(grid)
    if rows<2:
        return 0
    

    op_row=rows-1


    op=None
    for c in range(start,end+1):
        ch=grid[op_row][c]
        if ch in ("+","*"):
            op=ch
            break
    

    if op is None:
        return 0
    

    numbers=[]

    for c in range(end,start-1,-1):
        digits=[]

        for r in range(0,op_row):
            ch=grid[r][c]
            if ch !=" ":
                digits.append(ch)

            
        if digits:
            num=int("".join(digits))

            numbers.append(num)
    if not numbers:
        return 0
    
    if op=="+":
        return sum(numbers)
    
    prod=1
    for x in numbers:
        prod*=x
    
    return prod


def solve(path="input6.txt"):
    grid=parse_grid(path)
    segments=find_problem_segments(grid)

    total=0
    for start,end in segments:
        total+=eval_problem_columnwise(grid,start,end)
    return total


if __name__=="__main__":
    print(solve())