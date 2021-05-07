import sys
read = sys.stdin.readline

N = int(read()) # 크레인 수
crane = list(map(int, read().split())) # 무게 제한
M = int(read()) # 박스의 수
weight = list(map(int, read().split())) # 박스 무게

crane.sort(reverse=True)
weight.sort(reverse=True)
sec = 0
if max(weight) > max(crane):
    print(-1)
else:
    idx = 0
    while idx < len(weight):
        for i in range(len(crane)):
            for j in range(len(weight)):
                if crane[i] >= weight[j]:
                    idx += 1
                    break
        sec += 1

    print(sec)