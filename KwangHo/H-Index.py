def solution(citations):
    citations.sort() #내장함수 정렬
    answer = 0
    for i in range(0,len(citations)): # 0~리스트길이
        if len(citations)-i <= citations[i] : #인용 최소화 기준으로 맞쳐야 h번 인용이 딱 맞아 떨어진다.
            answer = len(citations)-i         #그래서 현재부터~끝까지의 길이와 인용횟수를 비교한다.
            break                             #길이를 넣어주고 나오면 끝!!
        
    return answer

'''
이문제는 H-Index이해하는데 한참걸렸다.(생소)
요점은
1. h번 인용 h번
2. 그리고 이 h번 인용이 최소화
문제이해한 후로는 잘 풀렸다.
'''