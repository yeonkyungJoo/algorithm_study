# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    '''
    방식1:
    차례대로 이동하면서 알파벳을 변경
    - 왼쪽/오른쪽 어디로 옮겨야될지 결정
    - 위/아래 어디로 옮겨야될지 결정
    
    방식2:
    각 문자열에 대해서 위/아래 횟수 계산
    - alhpa = 'abcdefghijklmnopqrstuvwxyz'
    - a -> x 로 움직여야하는 최소 횟수로 반환
    - x의 +index, -index만큼: index = alpha.index(x) / minus_index = index - 26 
    - index, minus_index 절대값 중에 적은 값으로 사용
    마지막에 좌/우로 움직여야하는 횟수 계산 (무조건 좌우 한방향이기 때문에 더 적게 움직여도 되는 방향으로 결정)
    - JABCD
    - JABCAD
    - JCDEF
    - JDFEAEI
    - JEDFA
    - a가 s[1](두번째)에 있으면 <-, s[-2](뒤에서 두번째)에 있으면 ->, len(name)-2
    - 나머지는 동일 (len(name)-1)
    '''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 상하 계산
    total = 0
    for s in name:
        index = alpha.index(s)
        minus_index = index - 26
        total += min((index, abs(minus_index)))
        
    total += (len(name) - 1)
    if 'A' in [name[1], name[-2]]:
        total -= 1
    # 좌우 계산
    return total

# 위 방식대로 풀었더니 10, 11번 에러
# 한쪽 방향으로 가지 않고 중간에 왔다갔다 하는 경우에 실패한 것으로 추정
# 돌아오는 방식도 고려해야함
