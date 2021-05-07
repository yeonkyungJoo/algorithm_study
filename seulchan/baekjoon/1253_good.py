'''
어떤 수가 다른 수 두개의 합으로 나타낼 수 있따면 good
-10**10 <= A <= 10**10

# solution
## brute force: O(n**3) -> x

## sort + loop +  two pointer
- sort
- loop
- create array without target
- two pointer

arr.sort()
answer = 0

for i in range(N):
    without_target = arr[:i] + arr[i+1:]
    left, right = 0, N-2
    while left < right:
        check_target = without_target[left] + without_target[right]
        if check_target == arr[i]:
            answer += 1
            break
        if check_target < arr[i]:
            left += 1
        else:
            right -= 1
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(N):
    without_target = arr[:i] + arr[i+1:]
    left, right = 0, N-2
    while left < right:
        check_target = without_target[left] + without_target[right]
        if check_target == arr[i]:
            answer += 1
            break
        if check_target < arr[i]:
            left += 1
        else:
            right -= 1

print(answer)
