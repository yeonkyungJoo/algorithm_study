def solution(files):
    answer = []

    for file in files:
        tmp = []
        i = 0
        head = "";
        while i <= len(file)-1 and not file[i].isnumeric():
            head += file[i]
            i += 1
        tmp.append(head)

        number = "";
        while i <= len(file)-1 and file[i].isnumeric():
            number += file[i]
            i += 1
        tmp.append(number)
        tmp.append(file[i:])

        answer.append(tmp)
    answer = sorted(answer, key=lambda x:(x[0].upper(), int(x[1])))
    result = []
    for arr in answer:
        result.append(''.join(arr))

    return result

if __name__ == "__main__":
    files = ["F-15"]
    print(solution(files))