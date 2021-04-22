'''
input:
- int: 1 <= N <= 50
- list:  max weigth for crane
- int: 1 <= M <= 10000
- list: weight of boxes

output:
- int: 모든 박스를 배로 옮기는데 드는 최솟값, 모두 옮길 수 없으면 -1

모두 옮길 수 없는 경우?
- 가장 큰 크레인보다 더 무거운 박스가 있는 경우 -> -1

# solution
## pseudocode

cranes.sort()
boxes.sort()

if cranes[0] < boxes[0]:
    return -1

boxes.reverse()  # reverse box (or can make queue) to pop from the end

count = 0
while_loop_count = 0
while boxes:
    # find index of next crain
    idx = while_loop_count % n
    next_crain = cranes[idx]

    box_idx = len(boxes) - 1

    while box_idx >= 0:
        next_box = boxes[box_idx]
        # 박스가 크레인에 실리면 박스를 꺼냄
        if next_crain > next_box:
            boxes.pop()
            break
        else:  # 안실리면 다음 박스 확인
            box_idx += 1
            continue

    while_loop_count += 1  # 다음 loop를 위해 loop 증가
    # crain 한바퀴 돌았으면 count 증가
    if idx == n-1:
        count += 1

-> log(m**2)
'''

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

def solution(n: int, m: int, cranes: list, boxes: list) -> int:
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    if cranes[0] < boxes[0]:
        return -1
    else:
        count=0
        while boxes:
            count+=1
            for i in cranes:
                if not boxes:
                    break
                else:
                    for j in range(len(boxes)):
                        if boxes[j] <= i:
                            boxes.pop(j)
                            break
        return count

print(solution(n, m, cranes, boxes))

if __name__ == '__main__':
    print(solution(3, 5, [6, 8, 9], [2, 5, 2, 4, 7]))

'''
디버깅이 너무 어려워 문제풀이보다 뭐가 잘못되었는지 찾는데 시간을 훨씬 더 많이 씀
'''
