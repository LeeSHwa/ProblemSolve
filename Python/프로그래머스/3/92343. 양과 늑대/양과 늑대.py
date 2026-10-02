from collections import defaultdict
    
def solution(info, edges):
    
    tree = defaultdict(list)
    
    for parent, child in edges:
        tree[parent].append(child)
    
    max_sheep = 0
    
    def dfs(sheep, wolf, next_nodes):
        nonlocal max_sheep
        
        max_sheep = max(max_sheep, sheep)
        
        for i, node in enumerate(next_nodes):
            nxt = next_nodes[:i] + next_nodes[i+1:] + tree[node]
            
            if info[node] == 0:
                dfs(sheep + 1, wolf, nxt)
            else:
                if sheep > wolf + 1:
                    dfs(sheep, wolf + 1, nxt)
                else:
                    continue

    dfs(1, 0, tree[0])
    
    return max_sheep