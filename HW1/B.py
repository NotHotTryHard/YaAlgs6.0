def func():
    A, B = int(input()), int(input())
    C, D = int(input()), int(input())
    
    sum1, sum2 = 0, 0
    M1, M2, N1, N2 = 0, 0, 0, 0
    
    
    if not A:
        return 1, C + 1
    elif not C:
        return A + 1, 1
    elif not B:
        return 1, D + 1
    elif not D:
        return B + 1, 1
    else:
        if max(A, B) <= max(C, D):
            M1 = max(A, B) + 1
            N1 = 1
            sum1 = M1 + N1
        else:
            M1 = 1
            N1 = max(C, D) + 1
            sum1 = M1 + N1
        
        if B + D + 2 <= A + C + 2:
            M2 = B + 1
            N2 = D + 1
            sum2 = M2 + N2
        else:
            M2 = A + 1
            N2 = C + 1
            sum2 = M2 + N2
        
        if sum1 <= sum2:
            return M1, N1
        else:
            return M2, N2
        
if __name__ == '__main__':
    print(*func())