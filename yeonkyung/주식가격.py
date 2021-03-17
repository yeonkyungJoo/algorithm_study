def solution(prices):
    answer = [0] * len(prices)
    # 기간 차이를 계산해야 하므로 인덱스를 추가
    stack = []

    for idx, price in enumerate(prices):
        while stack:
            if prices[stack[-1]] > price:
                last = stack.pop()
                answer[last] = idx - last
            else:
                break
        stack.append(idx)

    while stack:
        last = stack.pop()
        answer[last] = idx - last

    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))