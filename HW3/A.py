def func(s):
    stack = []
    opens = ['(', '{', '[']
    closings = [')', '}', ']']
    mapp = {opens[i] : closings[i] for i in range(len(opens))}
    for i in s:
        if i in opens:
            stack.append(i)
        elif i in closings:
            if not stack:
                return 'no'
            last = stack.pop()
            if mapp[last] != i:
                return 'no'

    if not stack:
        return 'yes'
    else:
        return 'no'
        
    
if __name__ == '__main__':
    s = input()
    print(func(s))