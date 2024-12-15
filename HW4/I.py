from collections import defaultdict, deque
#from tqdm import tqdm
from copy import copy
def find_diameter(N, edges):
    tree = defaultdict(list)
    #print(edges)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
        
    #print(tree)

    def bfs(start, block_list=[]):
        dist = [-1] * (N + 1)
        parent = [-1] * (N + 1)
        dist[start] = 0
        queue = deque([start])
        farthest_node = start

        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor in block_list:
                    continue
                elif dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    parent[neighbor] = node
                    queue.append(neighbor)
                    farthest_node = neighbor

        return farthest_node, dist, parent
    
    def bbfs(start_list, block_set=set([])):
        dist = [-1] * (N + 1)
        parent = [-1] * (N + 1)
        for start in start_list:
            dist[start] = 0
        queue = deque(start_list)
        
        farthest_node_1 = {}
        dist1 = defaultdict(int)
        farthest_node_2 = {}
        dist2 = defaultdict(int)
        
        back_list = []

        #print(block_set)
        #for root_num in tqdm(range(len(start_list))):
        for root_num in range(len(start_list)):
            root = start_list[root_num]
            max_dist = 0
            back_list_tmp = []
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor in block_set:
                        continue
                    elif dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        if dist[neighbor] > max_dist:
                            max_dist = dist[neighbor]
                            back_list_tmp = [(neighbor, root)]
                        elif dist[neighbor] == max_dist:
                            back_list_tmp.append((neighbor, root))

                        #parent[neighbor] = node
                        queue.append(neighbor)
                        #farthest_node_1[root] = neighbor
                        dist1[root] = dist[neighbor]
            back_list += back_list_tmp

        #back_list = list(farthest_node_1.values())
        #print(farthest_node_1)
        #print(dist1)
        #print(back_list)
        
        
        dist = [-1] * (N + 1)
        parent = [-1] * (N + 1)
        
        for root, source in back_list:
            distt = dist
            distt[root] = 0
            queue = deque([root])
            
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor in block_set:
                        continue
                    elif distt[neighbor] == -1:
                        distt[neighbor] = distt[node] + 1
                        #parent[neighbor] = node
                        queue.append(neighbor)
                        if dist2[source] < distt[neighbor]:
                            farthest_node_1[source] = root
                            farthest_node_2[source] = neighbor
                            dist2[source] = distt[neighbor]
                        
        #print(farthest_node_2)
        #print(dist2)
        data = {}
        for node in start_list:
            if node in dist1:
                data[node] = [dist1[node], dist2[node]]
        return data

    node1, _, _ = bfs(1)
    node2, _, parent = bfs(node1)

    
    path = []
    current = node2
    while current != -1:
        path.append(current)
        current = parent[current]
    
    #path = [12, 7, 3, 1, 2 , 4, 8, 13]
    #print(path)
    
    data = bbfs(path, set(path))
    #print(data)

    data1 = []
    data2 = []
    
    for node in path:
        if node in data:
            data1.append(data[node][0])
            data2.append(data[node][1])
        else:
            data1.append(0)
            data2.append(0)
    #print(data1)
    #print(data2)
    
    answ2 = max(data2) * (len(path) - 1)
    
    leftlen = 0
    leftArr = []
    rightlen = 0
    rightArr = []
    for i in range(len(path)):
        leftlen = max(leftlen, i + data1[i])
        leftArr.append(leftlen)
    for i in range(len(path)):
        rightlen = max(rightlen, i + data1[-i - 1])
        rightArr.append(rightlen)
    rightArr.reverse()
    
    answ1 = 0
    for i in range(len(path) - 1):
        answ1 = max(answ1, leftArr[i] * rightArr[i + 1])
    #print(leftArr)
    #print(rightArr)
    answ = max(answ1, answ2)
    print(answ)
    
    return answ
    '''data = []
    data1 = []
    data2 = []
    for node_num in tqdm(range(len(path))):
        block_list = []
        if node_num != 0:
            block_list.append(path[node_num - 1])
        if node_num != len(path) - 1:
            block_list.append(path[node_num + 1])
        node1, dist1, _ = bfs(path[node_num], path)
        node2, dist2, parent = bfs(node1, path)
        data.append((node1, node2, max(dist1), max(dist2)))
        data1.append(max(dist1))
        data2.append(max(dist2))
        
    answ2 = max(data2) * (len(path) - 1)
    
    leftlen = 0
    leftArr = []
    rightlen = 0
    rightArr = []
    for i in range(len(path)):
        leftlen = max(leftlen, i + data1[i])
        leftArr.append(leftlen)
    for i in range(len(path)):
        rightlen = max(rightlen, i + data1[-i - 1])
        rightArr.append(rightlen)
    rightArr.reverse()
    
    answ1 = 0
    for i in range(len(path) - 1):
        answ1 = max(answ1, leftArr[i] * rightArr[i + 1])

    return len(path) - 1, path, data, leftArr, rightArr, max(answ1, answ2)'''


# Пример использования
N = 15
edges = [
    (1, 2),
    (2, 4),
    (4, 8),
    (8, 13),
    (4, 9),
    (9, 14),
    (2, 5),
    (5, 10),
    (10, 15),
    (1, 3),
    (3, 6),
    (6, 11),
    (3, 7),
    (7, 12),
]

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

#diameter_length, path, data, leftArr, rightArr, answ = find_diameter(N, edges)
find_diameter(N, edges)
#print(answ)
'''print("Длина диаметра:", diameter_length)
print("Вершины на диаметре:", path)
print("Информация по вершинам:", data)
print("Если идем слева:", leftArr)
print("Если идем справа:", rightArr)
print("ОТВЕТ:", answ)
# Чтение данных
import sys
input = sys.stdin.read 
data = input().splitlines()
N = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:]]

# Вывод результата
print(find_max_product(N, edges))'''