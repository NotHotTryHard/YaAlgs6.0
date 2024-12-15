from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def func():
    n = int(input())
    name_list = []
    set1 = set()
    set2 = set()
    for _ in range(n - 1):
        a, b = input().split()
        set1.add(a)
        set2.add(b)
        name_list.append([a, b])
    
    papa = (set2 - set1).pop()
    tree = defaultdict(list)

    for child, parent in name_list:
        tree[parent].append(child)
    
    child_count = {}

    def rec(node):
        count = len(tree[node])
        for child in tree[node]:
            count += rec(child)
        child_count[node] = count
        return count
    rec(papa)
    
    for name in sorted(child_count):
        print(name, child_count[name])
 
    
if __name__ == '__main__':
    func()