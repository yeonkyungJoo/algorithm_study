def solution(s):
    answer = ''
    
    arr=""
    isChk = False
    
    for i in s:
        if not isChk and i!=" ":
            if not i in "0123456789":
                i= i.upper()
            isChk = True
        else :
            if i == " ":
                isChk = False
            else :
                i=i.lower()
            
        arr+=i
    answer = arr
    return answer

'''
문제가 짧아서 좋았다!

1. 공백이아니고 숫자가 아니라면 대문자로
2. 공백이면 다음나올 소문자 대문자 만들 불변수
3. 이외 대문자들은 소문자로

'''