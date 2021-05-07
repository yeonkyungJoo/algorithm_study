def solution(msg):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = dict()
    for idx, ch in enumerate(alphabet):
        dictionary[ch] = idx + 1

    def recursive(i):
        if i >= len(msg):
            return

        j = 1
        word, next = None, None
        while j <= len(msg) - i:
            if msg[i:i + j] not in dictionary:
                next = msg[i:i + j]
                break
            else:
                word = msg[i:i + j]
            j += 1

        answer.append(dictionary[word])
        dictionary[next] = len(dictionary) + 1
        recursive(i+(j-1))

    recursive(0)
    return answer


if __name__ == "__main__":
    msg = "ABABABABABABABAB"
    print(solution(msg))
