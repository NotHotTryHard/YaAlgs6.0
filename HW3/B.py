def func(n, a):
    prev = float('-inf')
    stack = []
    answ = [0] * n
    
    for i in range(n):
        if a[i] >= prev:
            stack.append(i)
        else:
            while stack:
                j = stack.pop()
                if a[j] > a[i]:
                    answ[j] = i
                else:
                    stack.append(j)
                    break
            stack.append(i)
        prev = a[i]
    for j in stack:
        answ[j] = -1
    return ' '.join(map(str, answ))
        
    
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(func(n, a))