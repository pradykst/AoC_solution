def count_splits(grid):
    rows=len(grid)
    cols=len(grid[0]) if rows else 0


    sr=sc=None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="S":
                sr,sc=r,c
                break
        if sr is not None:
            break

    
    if sr is None:
        raise ValueError("No S in grid")

    

    active={sc}

    splits=0

    for r in range(sr+1,rows):
        next_active=set()

        for c in active:
            if not (0<=c<cols):
                continue
        

            cell=grid[r][c]

            if cell=="^":
                splits+=1
                if c-1>=0:
                    next_active.add(c-1)
                if c+1<cols:
                    next_active.add(c+1)

            else:
                next_active.add(c)

        active=next_active

        if not active:
            break
    return splits



def main():
    with open("input7.txt","r") as f:
        grid=[list(line.rstrip("\n")) for line in f if line.strip() !=""]

    print(count_splits(grid))


if __name__=="__main__":
    main()
