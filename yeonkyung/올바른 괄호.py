def solution(s):
    s = list(s)
    stack = []

    if len(s) == 1:
        return False

    if s and s[-1] == "(":
        return False

    for e in s:
        if e == "(":
            stack.append(e)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True

if __name__ == "__main__":
    s = "(())()"
    print(solution(s))