def func(n, c, s):
    count_a = 0
    count_b = 0
    gr = 0
    maxlen = 1
    
    i, j = 0, 0
    if s[0] == 'a':
        count_a += 1
    elif s[0] == 'b':
        count_b += 1
    
    
    while True:
        if j == n - 1:
            break
        if gr <= c:
            j += 1
            if s[j] == 'a':
                count_a += 1
            elif s[j] == 'b':
                count_b += 1
                gr += count_a
            if gr <= c:
                maxlen = max(maxlen, j - i + 1)
        else:
            if s[i] == 'a':
                count_a -= 1
                gr -= count_b
            elif s[i] == 'b':
                count_b -= 1
            i += 1
            if i > j:
                j += 1
                if s[j] == 'a':
                    count_a += 1
                elif s[j] == 'b':
                    count_b += 1
                    gr += count_a
                
    return maxlen
            
        
    
if __name__ == '__main__':
    n, c = map(int, input().split())
    s = input()
    print(func(n, c, s))