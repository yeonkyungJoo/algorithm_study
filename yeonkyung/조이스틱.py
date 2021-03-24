def solution(name):
    idx, cnt = 0, 0
    distance = [min(ord(s) - ord("A"), ord("Z") - ord(s) + 1) for s in name]

    while True:
        cnt += distance[idx]
        distance[idx] = 0

        if sum(distance) == 0:
            break

        left, right = 1, 1

        while not distance[idx - left]:
            left += 1
        while not distance[idx + right]:
            right += 1

        if left >= right:
            idx += right
            cnt += right
        else:
            idx -= left
            cnt += left
    return cnt
