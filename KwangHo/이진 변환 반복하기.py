def solution(s):
    answer = []
    
    actionCnt = 0
    zeroCnt = 0
    
    while len(s)!=1 :
        t = s.count('0')
        n = len(s) - t
        s = str(bin(n)[2:])
        actionCnt+=1
        zeroCnt += t

    answer.append(actionCnt)
    answer.append(zeroCnt)
    return answer

'''
남은길이 = 전체길이 - 0의 길이
남은길이 2진수로 변환
횟수 카운팅
0의갯수 카운팅
문자열이 1까지 반복!!

'''