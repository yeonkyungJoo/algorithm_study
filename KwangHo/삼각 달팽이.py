def solution(n):
    answer = []
    state = 0 #0아래,1오른쪽,2대각선위로
    arr=[]
    ga=0
    se=0
    cnt=1

    arr = [[0] * n for i in range(n)]
    # 얕은복사로 리스트만들면 주소가 공유돼서
    # 반복문 돌면서 2차원배열 만듬!!
            
    for i in range(n):
        t1=0
        t2=0
        for j in range(n-i):
            if state==0: #밑으로
                arr[se+j][ga]=cnt
                t1=se+j
            elif state==1: #오른쪽으로
                arr[se][ga+j]=cnt
                t1=ga+j
            else : #위로
                arr[se-j][ga-j]=cnt
                t1=se-j
                t2=ga-j
            cnt+=1
        

        if state==0: #밑으로
            se=t1
            
            ga+=1
            state=1
        elif state==1: #오른쪽으로

            ga = t1-1
            se-=1
            state=2
        else : #위로
            se=t1+1
            ga=t2
            state=0 

    
    brr=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                brr.append(arr[i][j])
    answer=brr
    return answer

'''
3가지 패터이 반복
아래로갔다가 오른쪽으로 갔다가 대각선위로갔다가
t1,t2로 최근값 갱신 해주면서
상태가 끝나면 다음값으로 갱신하는 방법으로 품
'''