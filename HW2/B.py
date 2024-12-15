def twosum(n, k):
    count = 0
    numbers = [int(q) for q in input().split()]
    assert len(numbers) == n
    
    l, r = 0, 0
    s = numbers[0]

    while True:
        if s < k:
            if r < n - 1:
                r += 1
                s += numbers[r]
            else:
                break
        elif s == k:
            count += 1
            if l < r:
                s -= numbers[l]
                l += 1
            elif r < n - 1:
                r += 1
                s += numbers[r]
            else:
                break
        else:
            if l < r:
                s -= numbers[l]
                l += 1
            else:
                if r < n - 1:
                    r += 1
                    s += numbers[r]
                    s -= numbers[l]
                    l += 1
                else:
                    break
        #print(l, r, s)
    return count
            
            
if __name__ == '__main__':
    n, k = (int(q) for q in input().split())
    print(twosum(n, k))