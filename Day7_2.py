from collections import defaultdict

def count_timeline(grid):
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
        raise ValueError("No s in grid")

    


    ways={sc:1}

    for r in range(sr+1,rows):
        next_ways=defaultdict(int)

        for c,w in ways.items():
            if not (0<=c<cols):
                continue

            cell=grid[r][c]


            if cell=="^":
                if c-1>=0:
                    next_ways[c-1]+=w
                if c+1<cols:
                    next_ways[c+1]+=w
                
            else: 
                next_ways[c]+=w

        ways=next_ways

    return sum(ways.values())



def main():
    with open("input7.txt","r") as f:
        grid=[list(line.rstrip("\n")) for line in f if line.strip() !=""]

    print(count_timeline(grid))


if __name__=="__main__":
    main()

    


    