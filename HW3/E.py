def is_valid_expr(s):
        allowed_chars = set("0123456789+-*/() ")
        if not all(char in allowed_chars for char in s):
            return False
        tokens = s.split()
        for i in range(len(tokens) - 1):
            if tokens[i].isdigit() and tokens[i + 1].isdigit():
                return False
        return True

def func(s):
    try:
        if not is_valid_expr(s):
            return "WRONG"
        result = eval(s.replace(' ', ''))
        if not isinstance(result, int):
            return "WRONG"

        return result
    except Exception as e:
        return "WRONG"

if __name__ == '__main__':
    s = input().strip()
    print(func(s))

