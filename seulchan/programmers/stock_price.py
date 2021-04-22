# 이중 for문으로 다시 풀어봄. stack을 사용하고 싶었는데 잘 몰라서 못품
def solution(prices: list) -> list:
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    return answer

# 아래 방식으로 풀었을때에는 효율성 테스트 모두 걸림
def get_first_small_index(remain_prices: list, price: int, price_index: int) -> int:
    # 리스트에서 price보다 작은 값 중에 가장 먼저 나오는 값 찾는 함수
    # 해당 값이 아니라 index 반환
    # TODO: refactor
    # 가장 간단한 방법은 for문 돌리면서 나오는 작은 값 반환
    for i, p in enumerate(remain_prices):
        if price > p:
            return i + price_index + 1
    

def solution(prices):
    answer = []
    
    last_index = len(prices) - 1
    
    for i, price in enumerate(prices):
        remain_prices = prices[i+1:]
        if i == last_index:
            answer.append(0)
            continue
        if price <= min(remain_prices):
            answer.append(last_index - i)
            continue
        next_index = get_first_small_index(remain_prices, price, i)
        answer.append(next_index - i)
    return answer
