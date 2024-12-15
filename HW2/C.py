def func(n, r, numbers):
    count = 0
    i, j = 0, 1
    
    while i <= n - 2:
        while numbers[j] - numbers[i] <= r and j < n - 1:
            j += 1
        if numbers[j] - numbers[i] > r:
            count += n - j
        i += 1
    return count
            
if __name__ == '__main__':
    n, r = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(func(n, r, numbers))