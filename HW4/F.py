from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)


def func(corps, masters):
    graph = defaultdict(list)
    for i, master in enumerate(masters):
        graph[master - 1].append(i + 1)
    #graph[0].append(1)

    subtree_sizes = [0] * corps
    def dfs(node):
        subtree_size = 1
        count = 0
        for neighbor in graph[node]:
            subsubtree_size, subcount = dfs(neighbor)
            subtree_size += subsubtree_size
            count += subcount
        count += subtree_size
        subtree_sizes[node] = count
        return subtree_size, count
    
    sub_size = dfs(0)
    return subtree_sizes

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        corps = int(file.readline().strip())
        masters = map(int, file.readline().split())
    result = func(corps, masters)
    print(" ".join(map(str, result)))

'''
if __name__ == '__main__':
    corps = int(input())
    masters = map(int, input().split())
    result = func(corps, masters)
    print(" ".join(map(str, result)))'''


'''
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


def func(corps, masters):
    graph = defaultdict(list)
    for i, master in enumerate(masters):
        graph[master - 1].append(i + 1)
    #graph[0].append(1)
    
    subtree_sizes_x = [0] * corps
    subtree_sizes = [0] * corps
    #print(graph)
    def dfs(node, depth):
        subtree_size = depth
        for neighbor in graph[node]:
            subtree_size += dfs(neighbor, depth + 1)
        subtree_sizes[node] = subtree_size
        return subtree_size
    
    sub_size = dfs(0, 1)
    #for corp in range(corps):
        #subtree_sizes_x[corp] = dfs(corp, 1)
    return subtree_sizes

if __name__ == '__main__':
    corps = int(input())
    masters = map(int, input().split())
    result = func(corps, masters)
    print(" ".join(map(str, result)))

'''