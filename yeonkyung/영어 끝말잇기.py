def solution(n, words):

    i = 1
    before = words[0]
    while i < len(words):
        if before[-1] != words[i][0]:
            #print(i, words[i])
            break
        if words[i] in words[:i]:
            #print(i, words[i])
            break
        before = words[i]
        i += 1

    if i == len(words):
        return [0, 0]
    else:
        number, order = (i+1) % n, (i+1) // n + 1
        if (i+1) % n == 0:
            number = n
            order = (i+1) // n
        return [number, order]

if __name__ == "__main__":
    n = 2
    words = ["hello", "one", "even", "never", "now", "world", "draw"]
    print(solution(n, words))