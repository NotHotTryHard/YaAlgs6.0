from collections import deque

def func(n, k, a):
    answ = []
    deq = deque()
    

    for i in range(n):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        while deq and a[deq[-1]] > a[i]:
            deq.pop()
        deq.append(i)
        
        if i >= k - 1:
            answ.append(a[deq[0]])
    return '\n'.join(map(str, answ))
        
    
if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(func(n, k, a))