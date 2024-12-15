
def func():
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        name_list = [list(file.readline().split()) for _ in range(n - 1)]
        queries = [list(line.split()) for line in file]
    
    parents_dict = {}

    for child, parent in name_list:
        parents_dict[child] = parent
    
    def get_parents(node):
        parents = [node]
        cur_node = node
        while cur_node in parents_dict:
            cur_node = parents_dict[cur_node]
            parents.append(cur_node)
        return parents
    
    
    for c1, c2 in queries:
        par1 = get_parents(c1)
        par2 = get_parents(c2)
        #print(c1, c2)
        #print(par1, par2)
        
        k = len(par1) - 1
        while k > 0 and par1[k] in par2:
            k -= 1
        if par1[k] not in par2:
            k += 1
            
        print(par1[k])
 
    
if __name__ == '__main__':
    func()