def solution(p):
    p = list(p)
    if not p:
        return ""

    i = 0
    l, r = 0, 0
    while i <= len(p):
        if p[i] == "(":
            l += 1
        else:
            r += 1

        if l == r:
            break
        i += 1

    u = p[:i+1]
    v = p[i+1:]
    # print(u, v)
    stack = []
    for e in u:
        if e == "(":
            stack.append(e)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(e)
    if not stack:   # 올바른 괄호 문자열
        return ''.join(u) + solution(v)
    else:
        reversed_u = []
        for e in u[1:-1]:
            if e == "(":
                reversed_u.append(")")
            else:
                reversed_u.append("(")
        return "(" + solution(v) + ")" + ''.join(reversed_u)


if __name__ == "__main__":
    p = "()))((()"
    print(solution(p))