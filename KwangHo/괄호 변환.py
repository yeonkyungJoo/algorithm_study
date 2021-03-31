def isbalanced(s): #옆고닫고의 짝수 밸런싱이 맞는지
    chk =0
    for i in s:
        if i=='(': chk+=1
        elif i==')':chk-=1
    if chk == 0 : return True
    else : return False

def iscorrect(s): #완벽한 괄호인지?
    arr=[]
    arr.append(s[0])
    for i in range(1,len(s)):
        if len(arr)==0 or arr[-1]==')' or (arr[-1]=='(' and s[i]=='('):
            arr.append(s[i])
        else :
            arr.pop()
    if len(arr)==0 :
        return True
    else :
        return False

def solution(p):
    answer = ''
    u=''
    v=''
    
    if len(p)==0 or iscorrect(p) :
        return p
    
    for i in range(2,len(p)+1,2): #최소u와 나머지v나눈후
        if isbalanced(p[0:i]):
            u=p[0:i]
            v=p[i:len(p)]
            break
    
    if iscorrect(u): #u가 맞느지 확인해서 ok이면 u추가 해서 v재귀
        answer += u + solution(v)
    else :           #u가 틀리면 문제에 공식처럼 앞쪽으로 땡겨오고 뒤에 완성형을 만들어주는 신기!
        answer += '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i=='(' : answer+=')'
            else : answer+= '('
    
    return answer

'''
이번 문제는 개인적으로 힘든 문제중 하나였다.
어려운거 둘째치고 이해를 하지못해 검색의도움을 받았다.

그리고 젤작은 괄호까지 가서 문제처리 후 위로 올라가는
과정이 코드짤때는 체계적이지 못해 값이 자꾸 들렸었다.
테스트 케이스를 2 / 4 / 6 하나씩 올려가면서 테스트해
겨우 구조를 만들었다.
'''