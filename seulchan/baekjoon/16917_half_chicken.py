'''
양념치킨: A
후라이드: B
반반: C

양념치킨 최소 X마리, 후라이드 최소 Y마리
반반치킨 * 2 -> 양념1, 후라이드1
-> 구매 가능한 비용 최소값

input: int (A, B, C, X, Y)
output: int

1 <= A, B, C <= 5000
1 <= X, Y <= 100000

# solution

## conditional
- 반반: 양념or후라이드보다 저렴한경우에만 가능
    - 둘 다보다 저렴한경우: 겹치는 부분은 모두 반반으로 구매
    - 하나보다 저렴:
- 반반이 모두 비싼경우: 양념/후라이드로 구매

- 반반*2 > 양념+후라이드 then 반반
- min(남은치킨*한마리, 남은치킨*반마리*2)

pseudocode

if A + B < C*2:  # 따로가 저렴한 경우
    return (A*X + B*Y)

rest_price = A if X > Y else B
rest_count = abs(X-Y)

total_half_price = C * min(X, Y)
total_rest_price = min(rest_price * rest_count, 2 * C * rest_count)
return total_rest_price + total_rest_price

if X >= Y:  # X가 더 많은 경우
    rest = X - Y
    min(X*rest, 

## 한마리당 가능한 최소값 구해서 곱하기
ex) 1000, 2000, 3000, 4, 3

## brute force: 전부 계산한 이후 min 반환
- 반반을 살 경우에는 무조건 반반으로 꽉 채우는게 이득
- 반반 사는 케이스 + 후/양 사는 케이스 나눠서 계산 -> min 반환
- 두번계산해도 O(1)이기 때문에 상관없음
- -> 이렇게 계산하면 반반으로 전부 계산했을 경우 저렴한 케이스를 커버하지 못함

pseudocode

# 반반계산
half = min(X, Y)
half_count = half * 2
half_price = half_count * C

rest_price = 0
if X == Y:  # 같을 경우 rest X
    pass
if X > Y:  # x가 클 경우 (X-Y)*A
    rest_price = (X-Y)*A
if X < Y:  # y가 클 경우 (Y-X)*B
    rest_price = (Y-X)*B

# 따로계산
whole_price = (X*A) + (Y*B)

return min(whole_price, half_price+rest_price)
'''

def solution(A: int, B:int, C:int, X:int, Y:int) -> int:
    if A + B < C*2:  # 따로가 저렴한 경우
        return (A*X + B*Y)
    rest_price = A if X > Y else B
    rest_count = abs(X-Y)

    total_half_price = 2 * C * min(X, Y)
    total_rest_price = min(rest_price * rest_count, 2 * C * rest_count)
    return total_half_price + total_rest_price

if __name__ == '__main__':
    print(solution(1500, 2000, 500, 90000, 100000))
    print(solution(1500, 2000, 1600, 3, 2))
    print(solution(1500, 2000, 1900, 3, 2))

A, B, C, X, Y = map(int, input().split())
print(solution(A, B, C, X, Y))
