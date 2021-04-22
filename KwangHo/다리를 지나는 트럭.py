def solution(bridge_length, weight, truck_weights):
    answer = 0
    arr=[0]*bridge_length #다리길이

    while len(arr) != 0 : #다리 건너갈때까지
        arr.pop(0)
        if truck_weights and sum(arr) + truck_weights[0] <= weight:
            arr.append(truck_weights.pop(0))
        elif truck_weights :
            arr.append(0)
        answer+=1
    return answer
'''
남은트럭이 있으면 조건 보고 추가
그외 팝 하면커 카운트
그래서 다리에 아무것도 없으면 끝
'''