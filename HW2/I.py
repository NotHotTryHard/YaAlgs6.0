def func(n, a, b, ps):
    listA = sorted(list(zip(a, b, range(n, 0, -1))))
    listB = sorted(list(zip(b, a, range(n, 0, -1))))
    '''print("A:")
    for k in listA:
        print(k[0], k[1], n - k[2])
    print("B:")
    for k in listA:
        print(k[0], k[1], n - k[2])
    print("Answ:")'''
        
    done = set()
    
    answ = []
    for p in ps:
        if p == 0:
            while listA:
                _, _, tmp = listA.pop()
                alg = n - tmp 
                if alg not in done:
                    done.add(alg)
                    answ.append(alg + 1)
                    break
        elif p == 1:
            while listB:
                _, _, tmp = listB.pop()
                alg = n - tmp 
                if alg not in done:
                    done.add(alg)
                    answ.append(alg + 1)
                    break
    return ' '.join(map(str, answ))
            
            
    
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(func(n, a, b, p))
    
'''
5
1 2 3 4 5
5 4 3 2 1
1 0 1 0 0

6
3 10 6 2 10 1
3 5 10 7 5 9
0 0 1 1 0 1

5
1 2 2 2 1
5 2 3 2 1
1 0 1 0 0

3 
1 2 3
1 1 1
1 0 1

3 
1 1 1
1 2 3
1 0 1

3 
1 1 1
1 1 1
1 0 1
'''