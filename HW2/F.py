MOD = 1000000007

def func(n, nums):
    total = 0
    pairs = 0
    result = 0

    for i in range(n):
        result = (result + nums[i] * pairs) % MOD
        pairs = (pairs + nums[i] * total) % MOD
        total = (total + nums[i]) % MOD

    return result

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(func(n, nums))
