def solution(s):
    answer = []
    i = 0
    while i <= len(s) - 1:
        ch = s[i]
        if i == 0:
            ch = ch.upper()
        else:
            if s[i-1] == ' ':
                ch = ch.upper()
            else:
                ch = ch.lower()
        answer.append(ch)
        i += 1
    return ''.join(answer)

if __name__ == "__main__":
    s = "aa  bb"
    print(solution(s))
