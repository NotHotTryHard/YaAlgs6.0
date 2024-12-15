def func(n, nums):
    if n == 1:
        return nums
    nums.sort()
    if n % 2 == 1:
        l = r = n // 2
    else:
        r = n // 2
        l = r - 1
    
    answ = []
    while nums:
        if len(nums) % 2 == 1:
            answ.append(nums.pop(l))
            l -= 1
        else:
            answ.append(nums.pop(l))
            r -= 1
    return answ

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    print(*func(n, nums))