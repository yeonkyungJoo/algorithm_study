def solution(n, words):
    answer = []

    arr=[]
    a=0
    b=0
    
    arr.append(words[0])
    for i in range(1,len(words)):
        t = words[i]
        if len(t) > 1 and words[i-1][-1] == t[0] and t not in arr :
            arr.append(t)
        else :
            a = i%n +1
            b = i//n +1
            break
    
    answer.append(a)
    answer.append(b)
    return answer

'''
[조건]
1. 길이 1보다 큰지
2. 끝단어 == 첫단어
3. 중복체크
이외라면 틀렷으므로 출력
'''