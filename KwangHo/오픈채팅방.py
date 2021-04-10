def solution(record):
    answer = []
    arr=[] # 출입 스택
    brr={} # 최신 아이디값 저장
    
    for i in record:
        t = i.split(" ")        # 공백기준 3개로 나누고
        if t[0]=='Enter' : t[0]='님이 들어왔습니다.'    #문자변환
        elif t[0]=='Leave' : t[0]='님이 나갔습니다.'    #문자변환
        if t[0]!='Change' : arr.append([t[1],t[0]])  #변경제외 출입 스택 쌓기
        if len(t)==3 : brr[t[1]]=t[2]                #나감제외 아이디 갱신

    for i in arr:
        answer.append( brr[i[0]]+i[1] ) #아이뒤+문자 출력
        
    return answer