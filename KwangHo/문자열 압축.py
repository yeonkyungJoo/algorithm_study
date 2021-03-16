def solution(s):
    n = len(s) #문자열의 길이
    answer = n #최대값을 넣어준다
    
    for i in range(1,int(n/2+1)): #자를떄 1부터 ~ 절반까지
      dap = '' #임시값 초기화
      temp = s[0:i] #처음 자를값 초기화
      cnt = 1 #최소1개는 있으니 1로
      for j in range(i,n,i): #2개씩 자르면 2~끝까지-1, 2개씩 증가
        if temp == s[j:j+i]: #자른값이랑 나머지값들 비교
          cnt+=1 #같다면 +1
        else : #아니라면
          if cnt>1: dap+=str(cnt) #2개 이상이라면 같은값이 존재니깐 숫자추가
          dap += temp #자른값 추가
          temp = s[j:j+i] #같은 같이 없으니 다음값으로 자른값 갱신
          cnt = 1 # 최소1 초기화

      if cnt>1: dap+=str(cnt) #위와같음
      dap += temp #위와같음 => 한번 더써주는이유는 마지막 남은값 때문

      answer = min(answer,len(dap)) #작은값 찾기
    return answer

'''
처음 문제를 읽고 아하 이렇게 풀면되겟다.
했는데 머릿속과 의사코드로는 그려졌는데
막상 코드로 옮길려니깐 생각보다 잘 그려지지 않았고
파이썬 문법도 자꾸 틀려서 조금 해맸다.ㅠ
'''