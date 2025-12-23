import sys

                                                             
sys.setrecursionlimit(5000)

def solve():
                                                
                                          
    graph = {}
    
    try:
        with open('input11.txt', 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                
                                                                              
                source, dests_str = line.strip().split(':')
                
                                                                    
                neighbors = dests_str.strip().split()
                graph[source.strip()] = neighbors
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please save your puzzle input to this file.")
        return

                                                     
                                                               
    memo = {}

    def count_paths(node):
                                             
                                      
        if node == 'out':
            return 1
        
                                                         
        if node not in graph:
            return 0
        
                                                                
        if node in memo:
            return memo[node]

                                                      
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths(neighbor)
        
                                                        
        memo[node] = total_paths
        return total_paths

                                    
    if 'you' not in graph:
        print("Error: The starting node 'you' was not found in the input!")
        return

    result = count_paths('you')
    print(f"Total number of paths from 'you' to 'out': {result}")

if __name__ == "__main__":
    solve()