def solution(s):
    answer = 0
    arr=[]
    
    for i in s:
        if arr and arr[-1]==i:
            arr.pop()
        else :
            arr.append(i)

    if not arr : answer=1
    
    return answer

'''
s문자열 돌면서
하나씩 빼면서 비교해서 같으면 팝
다르면 추가하는 규칙으로!!

풀이법이 잘 떠올라서 바로 풀긴했는데
효율성에서 시간초과나서, 줄일수있는대로
줄였도 시간초과나서 왜그런가 했는데

★★문자열과 리스트의 속도차이가 많이 난다★★
:슬라이싱 , 추가/제거 쪽에서 속도차이가 나는거같다

아래는 문자열로 풀었을때

def solution(s):
    answer = 0
    t=''
    
    for i in s:
        if len(t)>0 and t[-1]==i:
            t=t[:-1]
        else :
            t+=i

    if not t : answer=1
    
    return answer
'''