from collections import deque

def func(n, H, heights, widths):
    chairs = sorted(list(zip(heights, widths)))
    #print(chairs)

    min_discomfort = float('inf')
    left = 0
    cur_width = 0
    deque_disc = deque()

    for right in range(n):
        cur_width += chairs[right][1]
        
        if right > 0:
            new_disc = abs(chairs[right][0] - chairs[right - 1][0])
            while deque_disc:
                if deque_disc[-1] < new_disc:
                    deque_disc.pop()
                else:
                    break
            deque_disc.append(new_disc)
        
        while cur_width >= H:
            if left == right:
                return 0
            
            min_discomfort = min(min_discomfort, deque_disc[0])
            cur_width -= chairs[left][1]
            
            if deque_disc[0] == abs(chairs[left + 1][0] - chairs[left][0]):
                deque_disc.popleft()
            left += 1

    return min_discomfort
    
    
if __name__ == '__main__':
    n, H = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    print(func(n, H, heights, widths))