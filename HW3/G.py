def func(n, b, a):
    num_now = 0
    time = 0
    for i in a:
        num_now += i
        time += num_now
        num_now = max(0, num_now - b)
    time += num_now
        
    return time
    

    
if __name__ == '__main__':
    n, b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(func(n, b, a))