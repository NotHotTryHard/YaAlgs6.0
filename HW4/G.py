from collections import defaultdict, deque
import math
import sys
#from tqdm import tqdm
sys.setrecursionlimit(10000000)

def find_connected_components_and_depth(N, M, K, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    
    visited = [False] * (N + 1)
    components = []
    depths = []
    diameters = []
    
    def bfs_farthest(node):
        queue = deque([(node, 0)])
        visited_local = {node}
        parent = {node: None}
        farthest_node, max_distance = node, 0
        
        while queue:
            current, distance = queue.popleft()
            farthest_node, max_distance = current, distance
            
            for neighbor in graph[current]:
                if neighbor not in visited_local:
                    visited_local.add(neighbor)
                    parent[neighbor] = current
                    queue.append((neighbor, distance + 1))
        
        path = []
        current = farthest_node
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        
        return farthest_node, max_distance, path

    
    #for i in tqdm(range(1, N + 1)):
    for i in range(1, N + 1):
        if not visited[i]:
            component = []
            farthest_node_1 = i
            max_depth = 0
            queue = deque([(i, 0)])
            visited[i] = True
            while queue:
                node, depth = queue.popleft()
                if depth > max_depth:
                    farthest_node_1 = node
                    max_depth = depth
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, depth + 1))
            components.append(component)
            farthest_node_2, depth, diameter = bfs_farthest(farthest_node_1)
            depths.append(depth)
            diameters.append(diameter)
    
    b = []
    for tmp in diameters:
        b += tmp
        
    for k in range(len(b)):
        i = b[k]
        for j in graph[i]:
            if k != len(b) - 1 and j == b[k + 1]:
                continue
            if k != 0 and j == b[k - 1]:
                continue
            if len(graph[j]) > 1:
                return [], None, None, None, None, None, 0
    
    mults = []
    ls = []
    rs = []
    dots = 0
    #for idx in tqdm(range(len(components))):
    for idx in range(len(components)):
        component = components[idx]
        diameter = diameters[idx]
        
            
        if len(diameter) == 1:
            dots += 1
            mults.append(1)
            ls.append(0)
            rs.append(0)
            continue
        elif len(diameter) == 2:
            mults.append(1)
            ls.append(1)
            rs.append(1)
            continue
        elif len(diameter) == 3:
            mult = int(math.factorial(len(component) - 1) % K / 2)
            mults.append(mult)
            ls.append(1)
            rs.append(len(component) - 1)
            continue
        
        color = 0
        mult = 1
        lr = [0, 0]
        
        for node in diameter[1:-1]:
            #print('NODE', node)
            count = len(graph[node]) - 2
            #print('COUNT', count)
            if node == diameter[1] or node == diameter[-2]:
                #print("ALT")
                count += 1
                
            
            mult = (mult * math.factorial(count)) % K # мб написать свой кастомный по модулю
            lr[color] += 1
            color = (color + 1) % 2
            lr[color] += count
            #print('LR', lr)
        mults.append(mult)
        ls.append(lr[0])
        rs.append(lr[1])
    mult = 1
    l = sum(ls)
    r = sum(rs)
    #for idx in tqdm(range(len(components))):
    for idx in range(len(components)):    
        component = components[idx]
        
        mult = (mult * mults[idx]) % K # варианты расстановки внутри компоненты связанности
        if len(component) > 2:
            mult = (mult * 4) % K # перевороты самой компоненты
        elif len(component) == 2:
            mult = (mult * 2) % K # перевороты самой компоненты
    mult = (mult * math.factorial(len(components) - dots)) % K # перестановки компонент
    placeholders = l + r + 2

    for i in range(dots):
        mult = (mult * placeholders) % K 
        placeholders += 1

    return components, depths, diameters, mults, ls, rs, mult

N = 16  # Количество дятлов
M = 12  # Количество ребер
K = 1000000000
edges = [
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 9),
    (9, 5),
    (5, 7),
    (7, 6),
    (7, 8),
    (8, 10),
    (8, 11),
    (8, 12),
    (15, 16),
]
N, M, K = map(int, input().split())

edges = []
for _ in range(M):
    a_i, b_i = map(int, input().split())
    edges.append((a_i, b_i))

components, depths, diameters, mults, ls, rs, mult = find_connected_components_and_depth(N, M, K, edges)

for i in range(len(components)):
    components[i].sort()

#print("Components:", components)
#print("Depths:", depths)
#print("Diameters:", diameters)
#print("Mults:", mults)
#print("Ls:", ls)
#print("Rs:", rs)
#print("ANSWER:", mult)
print(mult)