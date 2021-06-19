def check(stack):

    dic = {
        "[": "]",
        "(": ")",
        "{": "}",
    }

    tmp = []
    while stack:
        v = stack.pop()
        if v in ("]", ")", "}"):
            tmp.append(v)
        else:
            if not tmp:
                return False

            if tmp[-1] != dic[v]:
                return False
            tmp.pop()

    if len(tmp) == 0 and len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0

    stack = list(s)
    i = 0
    while i < len(s):

        if stack[0] not in ("]", ")", "}") and stack[-1] not in ("[", "(", "{"):
            if check(stack[:]):
                answer += 1

        v = stack.pop(0)
        stack.append(v)
        i += 1

    return answer


if __name__ == "__main__":
    s = "}}}"
    print(solution(s))