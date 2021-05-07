# https://programmers.co.kr/learn/courses/30/lessons/42587
# from collections import deque
# count = 1
# def solution(priorities: list, location: int) -> int:
#     '''
#     전체 정렬
#     - 정렬 되었을 때 기존 location이 어디에 있는지 알아야됨
#     - queue에 (n, i)의 튜풀을 넣으면 해결될듯?
#     정렬된 리스트의 location 반환
# 
#     -> 재귀로 풀고 싶었는데 테스트 대거 실패함
#     '''
#     global count
# 
#     # 처음 돌릴때 queue 형태로 만들어줌
#     if type(priorities) == list:
#         tmp = deque()
#         for i, q in enumerate(priorities):
#             tmp.append((q, i))
#         priorities = tmp
# 
#     queue = deque()
#     original = priorities.copy()
# 
#     for i, q in enumerate(priorities):
#         # p가 가장 크면 무조건 인쇄. 인쇄한 항목은 queue에 넣지 않음
#         if q[0] == max(original)[0]:
#             # location이랑 맞으면 그냥 반환
#             if q[1] == location:
#                 return count
#             count += 1
#         else:
#             # 그렇지 않으면 index를 포함하여 다시 queue에 넣음
#             queue.append((q[0], q[1]))
#         original.popleft()
#     return solution(queue, location)

def solution(priorities: list, location: int) -> int:
    answer = 0
    max_value = max(priorities)
    while True:
        value = priorities.pop(0)
        # 값이 최대보다 크면
        if value == max_value:
            # 인쇄
            answer += 1
            # 현재 location이 반환할때면 (0) 반환
            if location == 0:
                return answer
            # 아니라면 location에서 1 제외
            # 최대값 제거되었으니 다시 계산
            location -= 1
            max_value = max(priorities)
        else:
            # 값이 최대가 아니면 이후에 추가
            priorities.append(value)
            # 현재 location일 때면 location을 마지막으로 보냄
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
