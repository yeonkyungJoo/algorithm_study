def solution(bridge_length, weight, truck_weights):
    answer = 0

    time = []
    bridge = []
    total = 0
    while True:
        answer += 1

        for i in range(len(time)):
            time[i] += 1

        if time and time[0] == bridge_length:
            total -= bridge.pop(0)
            time.pop(0)
            if not time and not truck_weights:
                break

        if truck_weights and total + truck_weights[0] <= weight:
            time.append(0)
            next = truck_weights.pop(0)
            bridge.append(next)
            total += next

    return answer

if __name__ == "__main__":
    bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))
