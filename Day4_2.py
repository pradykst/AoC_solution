def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    removed = 0 

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbour_count = 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbour_count += 1
                       

            if neighbour_count < 4:
                removed+=1
                grid[r][c]="."

    return removed


def main():
    with open("input4.txt", "r") as f:
        grid = [list(line.strip()) for line in f if line.strip() != ""]
    
    total_removed=0
    while True:
        removed=count_accessible_rolls(grid)
        if removed==0:
            break
        total_removed+=removed

    print(total_removed)


if __name__ == "__main__":
    main()
