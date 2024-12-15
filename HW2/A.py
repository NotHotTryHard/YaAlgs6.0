def prefixsum(n):
    sum = 0
    arr = []
    for i in input().split():
        sum += int(i)
        arr.append(sum)
    return arr

if __name__ == '__main__':
    print(*prefixsum(int(input())))