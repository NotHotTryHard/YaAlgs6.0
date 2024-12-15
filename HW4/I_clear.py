from collections import defaultdict, deque
#from tqdm import tqdm
from copy import copy

def find_diameter(N, edges):
    # инициализируем дерево
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # обход в ширину из точки
    def bfs(start):
        dist = [-1] * (N + 1)
        parent = [-1] * (N + 1)
        dist[start] = 0
        queue = deque([start])
        furthest_node = start

        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if dist[neighbor] == -1: # если ещё не были, то входим в точку 
                    dist[neighbor] = dist[node] + 1
                    parent[neighbor] = node
                    queue.append(neighbor)
                    furthest_node = neighbor # так как обходим в ширину, последняя нода всегда "на последнем уровне" -- самая удаленная

        return furthest_node, dist, parent

    # это был обход в ширину из множества, но разросся до какой-то необзываемой колбасы
    def bbfs(start_list): 
        dist = [-1] * (N + 1)
        for start in start_list:
            dist[start] = 0
        queue = deque(start_list)
        
        furthest_node_1 = {}    # {node: node1} -- наиболее отдаленная от диаметра вершина node1 на отростке из вершины node, лежащей на диаметре
        dist1 = defaultdict(int)# {node: dist1} -- "глубина" отростка из вершины node, лежащей на диаметре
        furthest_node_2 = {}    # {node1: node2} -- наиболее отдаленная от диаметра вершина node2 на отростке из вершины node1
        dist2 = defaultdict(int)# {node1: dist2} -- "диаметр" отростка из вершины node (от node1 до node2)
        

        #for root_num in tqdm(range(len(start_list))):
        for root in start_list: # для каждго root на диаметре выполняем свой поиск "вбок"
            queue = deque([root])
            
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if dist[neighbor] == -1: # дальше по диаметру не пойдёт, останется в отростке
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
                        furthest_node_1[root] = neighbor
                        dist1[root] = dist[neighbor]

        back_list = list(furthest_node_1.values()) # самые глубокие от диаметра ноды 
        block_set = set(start_list)
                
        dist = [-1] * (N + 1)
        for start in back_list: # теперь начинаем обход из них
            dist[start] = 0
        
            queue = deque([root])
            
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor in block_set: # проверяем, что не вышли на диаметр
                        continue
                    elif dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
                        furthest_node_2[root] = neighbor
                        dist2[root] = dist[neighbor]
        data = {}
        for node in start_list: # если на вершине диаметра есть ненулевой отросток, то записываем его dist1 и dist2
            if node in furthest_node_1:
                data[node] = [dist1[node], dist2[furthest_node_1[node]]]
        
        
        return data

    node1, _, _ = bfs(1) 
    node2, _, parent = bfs(node1) # node1 - node2 - диаметр

    
    path = []
    current = node2
    while current != -1:
        path.append(current)
        current = parent[current] # собрали path - путь диаметра
    
    #path = [12, 7, 3, 1, 2 , 4, 8, 13]
    #print(path)
    
    data = bbfs(path) # получили длины этих "отростков"
    data1 = []
    data2 = [0]
    
    for node in path:
        if node in data:
            data1.append(data[node][0])
            data2.append(data[node][1])
        else:
            data1.append(0)
    
    answ2 = max(data2) * (len(path) - 1) # вариант где берём диагональ
    
    leftlen = 0
    leftArr = []
    rightlen = 0
    rightArr = []
    for i in range(len(path)):
        leftlen = max(leftlen, i + data1[i])
        leftArr.append(leftlen)
    for i in range(len(path)):
        rightlen = max(rightlen, i + data1[-i-1])
        rightArr.append(rightlen)
    rightArr.reverse()
    
    answ1 = 0
    for i in range(len(path) - 1):
        answ1 = max(answ1, leftArr[i] * rightArr[i + 1]) # вариант где главная диагональ "сворачивает"

    return max(answ1, answ2)



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

answ = find_diameter(N, edges)
print(answ)
