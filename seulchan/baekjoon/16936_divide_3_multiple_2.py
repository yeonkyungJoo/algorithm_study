'''
정수 x, N-1번 연산

divide 3: x / 3  (x % 3 == 0)
multiple 2: x * 2

ex. x = 9, N = 6, x2, x2, d3, x2, d3
A = [9, 9*2, 9*2*2, 9*2*2/3, 9*2*2/3*2, 9*2*2/3*2/3]
A = [3*3, 3*3*2, 3*3*2*2, 3*2*2, 3*2*2*2, 2*2*2]
A = [
    3*3, 3*3*2, 3*3*2*2  # 3: 2개, 2: +1
    3*2*2, 3*2*2*2,      # 3: 1개, 2: +1
    2*2*2                # 3: 0개, 2: +1
]
A = [9, 18, 36, 12, 24, 8]
B => randomize A

input: B
output: A

2 <= N <= 100
1 <= B[i] <= 10**18

-> sort with count of 3

## solution
- count number -> count of 3 & 2 -> python Counter? make helper function
- sort with count of 3

pseudocode

def calculate_count_3(x: int) -> int:
    # count 3
    3_count = 0
    while True:
        if x % 3 == 0:
            3_count += 1
            x = x // 3
        else:
            break
    return 3_count

count_and_origin = [
    (calculate_count_3(number), number)
    for number in numbers
].sort(key=lambda x: (-x[0], x[1]))

for tup in count_and_origin:
    print(tup[1])
'''
n = int(input())
numbers = list(map(int, input().split()))

def calculate_count_3(x: int) -> int:
    # count 3
    count = 0
    while True:
        if x % 3 == 0:
            count += 1
            x = x // 3
        else:
            break
    return count

count_and_origin = [
    (calculate_count_3(number), number)
    for number in numbers
]
count_and_origin.sort(key=lambda x: (-x[0], x[1]))

for tup in count_and_origin:
    print(tup[1])
