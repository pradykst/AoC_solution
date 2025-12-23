import sys

                                          
sys.setrecursionlimit(5000)

def solve_part2():
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
        print("Error: 'input.txt' not found.")
        return

                                               
    def count_paths_between(start_node, end_node):
                                                                
        memo = {}

        def _dfs(current):
                                                                
            if current == end_node:
                return 1
                                         
            if current not in graph:
                return 0
                                  
            if current in memo:
                return memo[current]

            total = 0
            for neighbor in graph[current]:
                total += _dfs(neighbor)
            
            memo[current] = total
            return total

                                                     
        if start_node not in graph and start_node != end_node:
            return 0
            
        return _dfs(start_node)

                                                       
                                                
    leg1 = count_paths_between('svr', 'dac')
    leg2 = count_paths_between('dac', 'fft')
    leg3 = count_paths_between('fft', 'out')
    total_scenario_a = leg1 * leg2 * leg3

                                                       
    leg4 = count_paths_between('svr', 'fft')
    leg5 = count_paths_between('fft', 'dac')
    leg6 = count_paths_between('dac', 'out')
    total_scenario_b = leg4 * leg5 * leg6

                      
    total_valid_paths = total_scenario_a + total_scenario_b
    
    print(f"Scenario A (svr->dac->fft->out): {total_scenario_a}")
    print(f"Scenario B (svr->fft->dac->out): {total_scenario_b}")
    print(f"Total paths visiting both: {total_valid_paths}")

if __name__ == "__main__":
    solve_part2()