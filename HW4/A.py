def func(n):
    name_list = []
    set1 = set()
    set2 = set()
    for i in range(n - 1):
        a, b = input().split()
        set1.add(a)
        set2.add(b)
        name_list.append([a, b])
    
    papa = (set2 - set1).pop()
    
    
    floors = {papa: 0}
    while len(name_list):
        remove_list = []
        for a, b in name_list:
            if b in floors:
                floors[a] = floors[b] + 1
                remove_list.append([a, b])
        
        for a, b in remove_list:
            name_list.remove([a, b])
    
    for name in sorted(floors):
        print(name, floors[name])
    
    
        
    
if __name__ == '__main__':
    n = int(input())
    func(n)