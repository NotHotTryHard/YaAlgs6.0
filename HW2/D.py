def func(n, k, tasks):
    tasks.sort()
    l, r = 0, 1
    maxcount = 1
    
    while l <= n - 2:
        while r < n and tasks[r] - tasks[l] <= k:
            r += 1
        maxcount = max(maxcount, r - l)
        l += 1
    return maxcount
if __name__ == '__main__':
    n, k = map(int, input().split())
    tasks = list(map(int, input().split()))

    print(func(n, k, tasks))