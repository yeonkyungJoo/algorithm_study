def solution(sticker):

    if len(sticker) == 1:
        return sticker[0]

    # index 0부터 시작
    dp0 = [0 for _ in range(len(sticker))]
    dp0[0], dp0[1] = sticker[0], sticker[1]
    for i in range(2, len(dp0)-1):
        if i <= 2:
            dp0[i] = dp0[i-2] + sticker[i]
        else:
            dp0[i] = max(dp0[i-3], dp0[i-2]) + sticker[i]

    # index 1부터 시작
    dp1 = [0 for _ in range(len(sticker))]
    dp1[0], dp1[1] = 0, sticker[1]
    for i in range(2, len(dp1)):
        if i <= 2:
            dp1[i] = dp1[i-2] + sticker[i]
        else:
            dp1[i] = max(dp1[i-3], dp1[i-2]) + sticker[i]

    return max(max(dp0), max(dp1))

if __name__ == "__main__":
    sticker = [1, 3]
    print(solution(sticker))