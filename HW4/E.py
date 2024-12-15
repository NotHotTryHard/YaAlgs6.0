from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


def func(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    subtree_sizes = [0] * (len(edges) + 1)
    
    def dfs(node, parent):
        subtree_size = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                subtree_size += dfs(neighbor, node)
        subtree_sizes[node - 1] = subtree_size
        return subtree_size
    
    sub_size = dfs(1, 0)
    return subtree_sizes

if __name__ == '__main__':
    vertices = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(vertices - 1)]
    result = func(edges)
    print(" ".join(map(str, result)))
