def solution(arr):
    answer = [0, 0]

    def recursive(r, c, length):

        if length == 1:
            if arr[r][c] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
            return

        total = 0
        for i in range(r, r+length):
            for j in range(c, c+length):
                total += arr[i][j]

        if total == 0:
            answer[0] += 1
            return
        elif total == length * length:
            answer[1] += 1
            return
        else:
            recursive(r, c, length // 2)
            recursive(r + length // 2, c, length // 2)
            recursive(r, c + length // 2, length // 2)
            recursive(r + length // 2, c + length // 2, length // 2)

    recursive(0, 0, len(arr))

    return answer

if __name__ == "__main__":
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(arr))