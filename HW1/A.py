def func():
    x1, y1 = int(input()), int(input())
    x2, y2 = int(input()), int(input())
    x, y = int(input()), int(input())
    
    if x <= x1:
        if y <= y1:
            return 'SW'
        elif y1 < y < y2:
            return 'W'
        elif y2 <= y:
            return 'NW'
    elif x1 < x < x2:
        if y <= y1:
            return 'S'
        elif y1 < y < y2:
            ValueError('Swimmer must be out of plot.')
        elif y2 <= y:
            return 'N'
    elif x2 <= x:
        if y <= y1:
            return 'SE'
        elif y1 < y < y2:
            return 'E'
        elif y2 <= y:
            return 'NE'
    
if __name__ == '__main__':
    print(func())