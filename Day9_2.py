#nice and lengthy

import sys

def solve():
    # 1. READ INPUT
    try:
        with open('input9.txt', 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("Error: input9.txt not found.")
        return

    # Parse coordinates
    points = []
    for line in data.split('\n'):
        if line.strip():
            x, y = map(int, line.strip().split(','))
            points.append((x, y))

    if not points:
        print("No data found.")
        return

    n = len(points)
    
    # 2. COORDINATE COMPRESSION
    # Get unique sorted coordinates to build our logic grid
    unique_x = sorted(list(set(p[0] for p in points)))
    unique_y = sorted(list(set(p[1] for p in points)))
    
    # Maps real coordinate -> grid index
    x_map = {val: i for i, val in enumerate(unique_x)}
    y_map = {val: i for i, val in enumerate(unique_y)}
    
    W = len(unique_x) - 1
    H = len(unique_y) - 1
    
    # 3. IDENTIFY VERTICAL EDGES
    # We need these to determine which grid cells are 'Inside' vs 'Outside'
    v_edges = []
    for k in range(n):
        p1 = points[k]
        p2 = points[(k + 1) % n]
        
        # Store vertical edges: (x, y_min, y_max)
        if p1[0] == p2[0]:
            v_edges.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
    
    # 4. BUILD VALIDITY GRID (SWEEP LINE)
    # bad_grid[j][i] = 1 if the region is OUTSIDE, 0 if INSIDE
    # The region is: x range [unique_x[i], unique_x[i+1]], y range [unique_y[j], unique_y[j+1]]
    bad_grid = [[0] * W for _ in range(H)]
    
    for j in range(H):
        y_bottom = unique_y[j]
        y_top = unique_y[j+1]
        
        # Find edges that span this specific grid row
        active_edges = [ve[0] for ve in v_edges if ve[1] <= y_bottom and ve[2] >= y_top]
        active_edges.sort()
        
        is_inside = False
        edge_ptr = 0
        
        for i in range(W):
            x_curr = unique_x[i]
            
            # If we hit an edge at this X, toggle inside/outside status
            while edge_ptr < len(active_edges) and active_edges[edge_ptr] == x_curr:
                is_inside = not is_inside
                edge_ptr += 1
            
            # If we are NOT inside the polygon, this region is BAD (1)
            if not is_inside:
                bad_grid[j][i] = 1
    
    # 5. PREFIX SUMS (for O(1) area checking)
    # P[j][i] stores the sum of bad cells in the rectangle from (0,0) to (j-1, i-1)
    P = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            P[r+1][c+1] = P[r][c+1] + P[r+1][c] - P[r][c] + bad_grid[r][c]

    def count_bad_regions(c1, r1, c2, r2):
        """Returns number of bad cells in grid window [c1..c2] x [r1..r2]"""
        return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

    # 6. FIND MAX RECTANGLE
    max_area = 0

    # Iterate through every pair of vertices (Red Tiles)
    for i in range(n):
        for k in range(i, n):
            p1 = points[i]
            p2 = points[k]
            
            # Calculate geometric area
            # Area formula for tiles: (|dx| + 1) * (|dy| + 1)
            x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            
            if area <= max_area:
                continue
            
            # Get grid indices
            xi1, xi2 = x_map[x_min], x_map[x_max]
            yi1, yi2 = y_map[y_min], y_map[y_max]
            
            valid = True
            
            # CHECK VALIDITY
            # Case A: It is a 2D Rectangle (width > 0 and height > 0)
            if xi1 < xi2 and yi1 < yi2:
                # We check the grid regions fully enclosed by these coordinates
                # Columns from xi1 to xi2-1, Rows from yi1 to yi2-1
                if count_bad_regions(xi1, yi1, xi2-1, yi2-1) > 0:
                    valid = False
            
            # Case B: It is a Vertical Line (width = 0)
            elif xi1 == xi2:
                # A vertical line is valid if it lies on a boundary OR inside valid space.
                # It is valid if either the region to its immediate left or right is valid.
                for r in range(yi1, yi2):
                    left_ok = (xi1 > 0) and (bad_grid[r][xi1-1] == 0)
                    right_ok = (xi1 < W) and (bad_grid[r][xi1] == 0)
                    if not (left_ok or right_ok):
                        valid = False
                        break
                        
            # Case C: It is a Horizontal Line (height = 0)
            elif yi1 == yi2:
                # A horizontal line is valid if the region above or below is valid.
                for c in range(xi1, xi2):
                    up_ok = (yi1 > 0) and (bad_grid[yi1-1][c] == 0)
                    down_ok = (yi1 < H) and (bad_grid[yi1][c] == 0)
                    if not (up_ok or down_ok):
                        valid = False
                        break
            
            if valid:
                max_area = area

    print(f"Max Area: {max_area}")

if __name__ == "__main__":
    solve()