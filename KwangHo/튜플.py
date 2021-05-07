import operator
def solution(s):
    answer = []
    arr={}
    
    t=''
    for i in s:
        if i in "0123456789":
            t+=i
        elif (i==',' or i=='}') and t!='':
            tt = int(t)
            if tt in arr:
                arr[tt]+=1
            else :
                arr[tt]=1
            t=''

    arr = sorted(arr.items(),key=operator.itemgetter(1),reverse=True)

    for i in arr:
        answer.append(i[0])

    return answer

'''
문자열로 받게되는 느낌이라서

1. 숫자로 다바꿔준뒤
2. 딕셔너리로 숫자 카운팅하고
3. value기준으로 정렬후 (많이 쓰인게 앞으로)
4. key출력

'''