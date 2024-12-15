def func(s):
    nums = []
    ops = ['*', '+', '-']
    for char in s:
        if char in ops:
            n2 = nums.pop()
            n1 = nums.pop()
            if char == '*':
                res = n1 * n2
            elif char == '+':
                res = n1 + n2
            elif char == '-':
                res = n1 - n2
            nums.append(res)
        else:
            nums.append(int(char))
    assert len(nums) == 1
    return nums[0]
            
    
if __name__ == '__main__':
    s = input().split()
    print(func(s))