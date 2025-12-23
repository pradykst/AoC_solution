                 

import sys

def solve():
                   
    try:
        with open('input9.txt', 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("Error: input9.txt not found.")
        return

                       
    points = []
    for line in data.split('\n'):
        if line.strip():
            x, y = map(int, line.strip().split(','))
            points.append((x, y))

    if not points:
        print("No data found.")
        return

    n = len(points)
    
                               
                                                           
    unique_x = sorted(list(set(p[0] for p in points)))
    unique_y = sorted(list(set(p[1] for p in points)))
    
                                        
    x_map = {val: i for i, val in enumerate(unique_x)}
    y_map = {val: i for i, val in enumerate(unique_y)}
    
    W = len(unique_x) - 1
    H = len(unique_y) - 1
    
                                
                                                                           
    v_edges = []
    for k in range(n):
        p1 = points[k]
        p2 = points[(k + 1) % n]
        
                                                 
        if p1[0] == p2[0]:
            v_edges.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
    
                                         
                                                              
                                                                                               
    bad_grid = [[0] * W for _ in range(H)]
    
    for j in range(H):
        y_bottom = unique_y[j]
        y_top = unique_y[j+1]
        
                                                     
        active_edges = [ve[0] for ve in v_edges if ve[1] <= y_bottom and ve[2] >= y_top]
        active_edges.sort()
        
        is_inside = False
        edge_ptr = 0
        
        for i in range(W):
            x_curr = unique_x[i]
            
                                                                       
            while edge_ptr < len(active_edges) and active_edges[edge_ptr] == x_curr:
                is_inside = not is_inside
                edge_ptr += 1
            
                                                                      
            if not is_inside:
                bad_grid[j][i] = 1
    
                                             
                                                                                   
    P = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            P[r+1][c+1] = P[r][c+1] + P[r+1][c] - P[r][c] + bad_grid[r][c]

    def count_bad_regions(c1, r1, c2, r2):
        """Returns number of bad cells in grid window [c1..c2] x [r1..r2]"""
        return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

                           
    max_area = 0

                                                        
    for i in range(n):
        for k in range(i, n):
            p1 = points[i]
            p2 = points[k]
            
                                      
                                                             
            x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            
            if area <= max_area:
                continue
            
                              
            xi1, xi2 = x_map[x_min], x_map[x_max]
            yi1, yi2 = y_map[y_min], y_map[y_max]
            
            valid = True
            
                            
                                                                     
            if xi1 < xi2 and yi1 < yi2:
                                                                               
                                                                   
                if count_bad_regions(xi1, yi1, xi2-1, yi2-1) > 0:
                    valid = False
            
                                                       
            elif xi1 == xi2:
                                                                                          
                                                                                           
                for r in range(yi1, yi2):
                    left_ok = (xi1 > 0) and (bad_grid[r][xi1-1] == 0)
                    right_ok = (xi1 < W) and (bad_grid[r][xi1] == 0)
                    if not (left_ok or right_ok):
                        valid = False
                        break
                        
                                                          
            elif yi1 == yi2:
                                                                                   
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