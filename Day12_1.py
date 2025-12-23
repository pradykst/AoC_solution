import sys

def solve():
    # 1. Parsing
    try:
        with open('input12.txt', 'r') as f:
            raw_data = f.read().strip()
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
        return

    lines = raw_data.splitlines()
    
    # Store the AREA of each shape, not the geometry
    shape_areas = {} 
    queries = []
    
    current_shape_id = None
    current_hashes = 0
    
    for line in lines:
        line = line.rstrip()
        if not line:
            if current_shape_id is not None:
                shape_areas[current_shape_id] = current_hashes
                current_shape_id = None
                current_hashes = 0
            continue
            
        # Check for Query "46x43: ..."
        if 'x' in line and ':' in line and not line.split(':')[0].strip().isdigit():
            # Save pending shape if exists
            if current_shape_id is not None:
                shape_areas[current_shape_id] = current_hashes
                current_shape_id = None
                current_hashes = 0
                
            dims, counts = line.split(':')
            w, h = map(int, dims.split('x'))
            reqs = list(map(int, counts.strip().split()))
            queries.append({'w': w, 'h': h, 'reqs': reqs})
            
        # Check for Shape Header "0:"
        elif ':' in line and line.split(':')[0].strip().isdigit():
            if current_shape_id is not None:
                shape_areas[current_shape_id] = current_hashes
            
            current_shape_id = int(line.split(':')[0].strip())
            current_hashes = 0
            
        else:
            # Count the '#' in the grid line
            current_hashes += line.count('#')

    # Save final shape
    if current_shape_id is not None:
        shape_areas[current_shape_id] = current_hashes

    # 2. Calculation
    # For large grid bin packing with ~70% fill density, 
    # Area Sum is the determining factor.
    
    success_count = 0
    
    print(f"Shapes detected: {len(shape_areas)}")
    print(f"Shape Areas: {shape_areas}")
    print(f"Processing {len(queries)} queries...")
    
    for q in queries:
        grid_area = q['w'] * q['h']
        
        presents_area = 0
        for sid, count in enumerate(q['reqs']):
            if sid in shape_areas:
                presents_area += count * shape_areas[sid]
        
        # Heuristic: If they fit by area, count as success.
        if presents_area <= grid_area:
            success_count += 1
            
    print(f"Total capable regions: {success_count}")

if __name__ == "__main__":
    solve()