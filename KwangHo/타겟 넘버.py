cnt=0
targetG=0
numbersG=[]

def dfs(n,s): # n:위치인덱스 , s:합
    global numbersG
    if n == len(numbersG) : # 마지막 길이에 왔으면
        global targetG
        if s == targetG : # 타겟과 같으면 카운트!!
          global cnt
          cnt+=1
        return
    dfs(n+1,s+numbersG[n]) # 다음배열인덱스와 현재값을 더해서 넘겨주기
    dfs(n+1,s-numbersG[n]) # 다음배열인덱스와 현재값을 빼서 넘겨주기

def solution(numbers, target): 
    global numbersG,targetG
    
    numbersG = numbers
    targetG = target
    
    dfs(0,0)
    
    answer = cnt
    return answer

'''
깊이 우선 탐색 문제라 유튜브 강의 한번 봐주고 시작했다.
함수에 변수를 달고 가면 속도가 느릴꺼 같아서
전역변수로 다 빼고 테스트 해보니 
변수 달고 다녔을 경우와 전역으로 다뻇을떄 후자가 0.05~0.20ms 더 빨랐다.
더하기와 빼기 2가지 종류만 있어서 2개 dfs함수 돌리고
끝지점에 왔을때 target과 같으면 카운트 하는 방식으로 풀었다.
'''