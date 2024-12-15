def func(n, a, m, k, xs):
    l = r = n - 1
    stoppers = [0] * n
    drop = 0
    carry = a[l]
    
    while True:
        if l > 0:
            l -= 1
        else:
            break
        
        if a[l] == carry:
            drop += 1
            
        elif a[l] > carry:
            for j in range(l + 1, r + 1):
                stoppers[j] = l + 1
            r = l
            drop = 0
        
        elif a[l] < carry:
            pass
        
        if drop > k:
            stoppers[r] = l + 1
            r -= 1
            while l + 1 <= r and a[r] != a[r + 1]:
                stoppers[r] = l + 1
                r -= 1
            drop -= 1

        carry = a[l]
    #print(stoppers)
    
    answ = []
    for x in xs:
        answ.append(stoppers[x - 1] + 1)
    return ' '.join(map(str, answ))
    
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(func(n, a, m, k, x))
    
'''
6
3 3 3 4 4 5
4 2
3 4 5 6


7
1 5 7 2 10 10 6
7 0
1 2 3 4 5 6 7

6
3 3 3 3 3 3
6 2 
1 2 3 4 5 6


def func(n, a, m, k, xs):
    starters = [0]
    jump = [n - 1]
    
    
    carry = 0
    prev = a[-1]
    for i in range(n - 2, -1, -1):
        if a[i] == prev:
            carry += 1
            jump.append(i)
        starters.append(carry)
        prev = a[i]
    
    while len(jump) < 2 * n:
        jump.append(0)
    jump[0] = jump[1] + 1
    starters.reverse()
    
    
    lastind = 0
    stoppers = [0]
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            lastind = i
        stoppers.append(lastind)
    #stoppers.reverse()

    stoppers2 = [0] * 7
    
    for i in range(n - 1, -1, -1):
        if k == 0:
            if jump[starters[i] + 1] != 0:
                stoppers2[i] = jump[starters[i] + 1] + 1
            else:
                stoppers2[i] = 0
        else:
            stoppers2[i] = jump[k]
        
        
    
    #print(jump)
    #print(starters)
    #print(stoppers)
    #print(stoppers2)
    
    answ = []
    for x in xs:
        tmp = max(stoppers[x - 1], stoppers2[x - 1])
        answ.append(tmp + 1)
    return ' '.join(map(str, answ))

'''