def solution(s):
    answer = True
    dap=[]
    
    if s[0]==")": # 첫값이 )라면 계신 불필요해서 리턴
        return False
    
    for i in s :
        if i == "(" :  # ( 는 추가
            dap.append(i)
        elif i == ")" and len(dap)>0 and dap[len(dap)-1] == "(" : # ) 는 스택이 0보다 크거나 + ( 라면 스택 팝
            dap.pop()
        else : 
            return False # 위 조건이 아니라면 리턴
            break
    
    if len(dap) > 0 : # 남아있는게 하나라도 있으면 False
        answer = False

    return answer

'''
열고닫기 한세트 구성이라 스택으로 차례대로
집어넣다가 세트나오면 없애주는 방식으로 하고
마지막에 스택에 0이면 올바른 괄호 !!
+ 중간중간 불필요한 계산으로 인한 종료점 추가
'''