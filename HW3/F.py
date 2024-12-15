def func(n, vals, start):
    answ = start
    mapp = {'[': ']', '(': ')'}
    
    stack = []
    for char in start:
        if char in ['(', '[']:
            stack.append(char)
        elif char in [')', ']'] and stack and mapp[stack[-1]] == char:
            stack.pop()
        else:
            raise ValueError(1)
    
    while len(answ) + len(stack) < n:
        for new_char in vals:
            if new_char in ['(', '[']:
                answ += new_char
                stack.append(new_char)
                break
            elif new_char in [')', ']']:
                if stack and mapp[stack[-1]] == new_char:
                    answ += new_char
                    stack.pop()
                    break
                else:
                    continue
            else:
                raise ValueError(2)
    
    while stack:
        answ += mapp[stack.pop()]
    return ''.join(answ)
    

    
if __name__ == '__main__':
    n = int(input())
    vals = list(input())
    start = input()
    print(func(n, vals, start))