def func(n, nums):
    left, right = [], []
    leftnum, rightnum = 0, 0
    leftcarry, rightcarry = 0, 0
    for i in range(n):
        left.append(leftcarry)
        leftnum += nums[i]
        leftcarry += leftnum
        
        right.append(rightcarry)
        rightnum += nums[n - i - 1]
        rightcarry += rightnum
        
    right.reverse()
    
    
    vals = [left[i] + right[i] for i in range(n)]
    return min(vals)
        
    
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(func(n, nums))