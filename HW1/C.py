def func():
    n = int(input())
    screen_tmp = []
    rects = []
    for i in range(n):
        screen_tmp.append(list(input()))
    
    up, down, left, right = -1, -1, -1, -1
    for i in range(n):
        for j in range(n):
            if screen_tmp[i][j] == '#':
                left = j if left == -1 else min(left, j)
                right = j if right == -1 else max(right, j)
                up = i if up == -1 else min(up, i)
                down = i if down == -1 else max(down, i)
    if up == -1 and down == -1 and left == -1 and right == -1:
        return 'X'
    screen = [row[left:right + 1] for row in screen_tmp[up:down + 1]]
    #print(screen)
    N = down - up + 1
    M = right - left + 1
    
    continueFlag = True
    while continueFlag:
        up, down = -1, -1
        left, right = -1, -1
        for i in range(N):
            for j in range(M):
                if screen[i][j] == '.' and left == -1:
                    #print('up', i)
                    #print('left', j)
                    left = j
                    up = i
                if screen[i][j] == '#' and left != -1:
                    #print('right', j - 1)
                    right = j - 1
                    break
                if i == N - 1 and j == M - 1 and left == -1:
                    #print('ContFlagSet')
                    continueFlag = False
            if left != -1:
                if right == -1:
                    right = M - 1
                    #print('right', M - 1)
                break
        if not continueFlag:
            #print('OutCont')
            continue
        for i in range(up + 1, N):
            if screen[i][left:right + 1] == ['#'] * (right - left + 1):
                down = i - 1
                #print('down', i - 1)
                break
            if left != 0 and screen[i][left - 1] != '#':
                #print('Out1')
                return 'X'
            if right != M - 1 and screen[i][right + 1] != '#':
                #print('Out2')
                return 'X'
            if screen[i][left:right + 1] != ['.'] * (right - left + 1):
                #print('Out3')
                return 'X'
        if up != -1 and down == -1:
            down = N - 1
            #print('down', N - 1)
        rects.append((up, down, left, right))
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                screen[i][j] = '#'
        #print(screen)
    if len(rects) == 0:
        return 'I'
    elif len(rects) == 1:
        up, down, left, right = rects[0]
        if up != 0 and down != N - 1 and left != 0 and right != M - 1:
            return 'O'
        elif up != 0 and down != N - 1 and left != 0 and right == M - 1:
            return 'C'
        elif up == 0 and down != N - 1 and left != 0 and right == M - 1:
            return 'L'
        else:
            return 'X'
    elif len(rects) == 2:
        up1, down1, left1, right1 = rects[0]
        up2, down2, left2, right2 = rects[1]
        if left1 == left2 and right1 == right2 and up1 == 0 and down2 == N - 1:
            return 'H'
        elif up1 != 0 and down1 < up2 and left1 == left2 and right1 != M - 1 and right2 == M - 1 and down2 == N - 1:
            return 'P'
        else:
            return 'X'
    else:
        return 'X'
    #print(rects)
    return 'Z'
'''
4
.##.
.##.
.##.
....

4
#..#
#..#
####
####

4
##..
##..
####
####

4
..##
..##
####
####

4
#.##
#.##
####
####

4
####
#.##
####
####

4
....
....
....
....

4
####
####
####
####

4
##..
##..
##..
##..

4
##..
##..
#...
##..

4
#...
##..
####
####

4
#...
####
####
####

4
#...
####
#...
####

4
##..
####
#...
#...

4
#.#.
.#.#
#.#.
.#.#
'''
    
        
if __name__ == '__main__':
    print(func())