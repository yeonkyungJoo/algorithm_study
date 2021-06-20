def solution(key, lock):

    M = len(key)
    N = len(lock)
    for _ in range(4):

        # 회전
        tmp = [[0 for _ in range(M)] for _ in range(M)]
        for n in range(M):
            for m in range(M):
                tmp[m][M - 1 - n] = key[n][m]
        key = tmp
        # print(key)

        bg = [[0 for _ in range(N + (M - 1) * 2)] for _ in range(N + (M - 1) * 2)]
        for i in range(len(bg) - M + 1):
            for j in range(len(bg) - M + 1):

                bg = [[0 for _ in range(N + (M - 1) * 2)] for _ in range(N + (M - 1) * 2)]

                # key
                for k in range(M):
                    for l in range(M):
                        bg[i+k][j+l] += key[k][l]

                # lock
                for k in range(N):
                    for l in range(N):
                        bg[N - 1 + k][N - 1 + l] += lock[k][l]

                # check
                check = True
                for k in range(N):
                    for l in range(N):
                       if bg[N - 1 + k][N - 1 + l] != 1:
                            check = False

                if check:
                    return True

    return False

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))

