def solution(brown, yellow):
    s = brown + yellow
    
    answer = []
    sero = 3        # 세로 최소 3
    garo = 999999   # 가로 초기값 큰값
    
    while sero <= garo :    # 세로가 더 작다면 반복
        if s % sero == 0 :  # 나누어 떨어 지면
            garo = s / sero
            if (2*garo + 2*sero - 4 == brown) and ((garo-2)*(sero-2)==yellow) : #공식에 부합하면 OK
                answer = [garo,sero] 
                break
        sero+=1 # 위조건 안맞으면 세로값 ++
    
    return answer

'''
세로길이가 최소3이니 가로길이가 세로보다 큰 선에서 
가로,세로 찾아준다음
갈색,노랑 공식을 풀어쓴다음 가로,세로를 적용한다.
찾았느면 최소에서 거슬로 온거니 끝!
'''