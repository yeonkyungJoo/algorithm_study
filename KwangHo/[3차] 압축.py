def solution(msg):
    answer = []
    dic = []
    t = ""
    for i in range(0,26): # 사전만들기 A~Z까지
        dic.append(chr(65+i))

    while len(msg)!=0:
        for i in range(len(dic)-1,-1,-1): # 모든 사전 반복
            l = len(dic[i]) # 사전의 길이
            if dic[i] == msg[:l]: # 사전과 msg의 처음부터 사전길이까지 비교해서 같다면
                dic.append(dic[i]+msg[l:l+1]) #현재+(현재+1) 사전에 추가
                  # 왜 이렇게 했나면 미리 슬라이싱 하면 0에 대한 조건문 추가 때문에
                msg = msg[l:]   #앞문자열자르고
                answer.append(i+1)    #위치 출력

                break
    return answer