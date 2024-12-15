def func(n):
    answ = []
    numstack = []
    prefsumstack = []
    
    for i in range(n):
        com = input()
        com_type = com[0]
        if com_type != '-':
            k = int(com[1:])
            
        if com_type == '+':
            numstack.append(k)
            prefsumstack.append((prefsumstack[-1] if prefsumstack else 0) + k)
                
        elif com_type == '-':
            num = numstack.pop()
            prefsumstack.pop()
            answ.append(num)
            
        elif com_type == '?':
            if k == len(numstack):
                ksum = prefsumstack[-1]
            else:
                ksum = prefsumstack[-1] - prefsumstack[-1 - k]
            answ.append(ksum)
        else:
            raise ValueError
    return '\n'.join(map(str, answ))
    
if __name__ == '__main__':
    n = int(input())
    res = func(n)
    if res:
        print(res)