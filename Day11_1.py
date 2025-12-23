import sys

# Increase recursion depth just in case the path is very long
sys.setrecursionlimit(5000)

def solve():
    # 1. Parse the input into a graph dictionary
    # Format: "node: neighbor neighbor..."
    graph = {}
    
    try:
        with open('input11.txt', 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                
                # Split "aaa: bbb ccc" -> source="aaa", destinations="bbb ccc"
                source, dests_str = line.strip().split(':')
                
                # Clean up whitespace and create a list of neighbors
                neighbors = dests_str.strip().split()
                graph[source.strip()] = neighbors
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please save your puzzle input to this file.")
        return

    # 2. Define the Recursive Counting Function (DFS)
    # memo stores the path count for nodes we've already solved
    memo = {}

    def count_paths(node):
        # Base Case 1: We reached the target!
        # This counts as 1 valid path.
        if node == 'out':
            return 1
        
        # Base Case 2: This node leads nowhere (dead end)
        if node not in graph:
            return 0
        
        # Optimization: Check if we already calculated this node
        if node in memo:
            return memo[node]

        # Recursive Step: Sum paths from all neighbors
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths(neighbor)
        
        # Store the result in our cache before returning
        memo[node] = total_paths
        return total_paths

    # 3. Start the search from 'you'
    if 'you' not in graph:
        print("Error: The starting node 'you' was not found in the input!")
        return

    result = count_paths('you')
    print(f"Total number of paths from 'you' to 'out': {result}")

if __name__ == "__main__":
    solve()