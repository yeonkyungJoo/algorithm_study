import sys
f = [0] * 1000001

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        f[j] += i
    f[i] = f[i-1] + f[i]

T = int(sys.stdin.readline())
for _ in range(T):
    print(f[int(sys.stdin.readline())])