def solution(numbers):
    answer = []
    for div in numbers:
        if div < 2:
            answer.append(div + 1)
            continue

        binary = []
        while div:
            div, mod = divmod(div, 2)
            binary.append(mod)

        for i in range(len(binary) - 1):
            if binary[i:i + 2] == [0, 0] or binary[i:i + 2] == [0, 1]:
                binary[i] = 1
                break

            if binary[i:i + 2] == [1, 0]:
                binary[i:i + 2] = [0, 1]
                break
        else:
            binary[-1] = 0
            binary.append(1)

        base10 = 0
        for i in range(len(binary)):
            base10 += binary[i] * 2 ** i
        answer.append(base10)
    return answer


if __name__ == "__main__":
    numbers = [2,7]
    print(solution(numbers))