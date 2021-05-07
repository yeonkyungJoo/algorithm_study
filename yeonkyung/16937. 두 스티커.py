H, W = map(int, input().split())
N = int(input())

size = []
for _ in range(N):
    size.append(tuple(map(int, input().split())))

#print(size)

def check(s1, s2):
    if max(s1[1], s2[1]) <= H and s1[0] + s2[0] <= W :
        return True
    if max(s1[0], s2[0]) <= W and s1[1] + s2[1] <= W :
        return True

    return False

answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        s1 = size[i]
        s2 = size[j]
        area = s1[0] * s1[1] + s2[0] * s2[1]

        for k in range(1 << 2):
            s1 = size[i]
            s2 = size[j]
            if 1 << 1 & k:
                s1 = list(reversed(size[i]))
            if 1 << 0 & k:
                s2 = list(reversed(size[j]))

            if check(s1, s2):
                answer = max(area, answer)

print(answer)