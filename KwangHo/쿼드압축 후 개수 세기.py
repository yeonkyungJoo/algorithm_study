def ReMake(arr,n,m,r): # 이건 배열구간 자르기 전체배열로 인덱스로 할려니 복잡해서
    t=[]
    for i in range(n,n+r):
        t.append([])
        for j in range(m,m+r):
            t[i-n].append(arr[i][j])
    return t
            

def QuadComp(arr):
    l = len(arr)
    l2=l*l

    cnt0 = 0
    cnt1 = 0

    for i in range(l): #현재 arr의 0의 개수와 1의 개수를 카운팅
        cnt0 += arr[i].count(0)
        cnt1 += arr[i].count(1)    

    if l2==4 : #쪼개질수없는 4개라면
        temp=[0,0]
        temp[0]=arr[0].count(0)+arr[1].count(0)
        temp[1]=arr[0].count(1)+arr[1].count(1)
        if temp[0] == 4 : temp[0]=1 #0이 4개라면 1로주고
        if temp[1] == 4 : temp[1]=1 #1이 4개라면 1로주고
        return temp 
    elif l2 == cnt0: #8,16,32일경우가 있으니 0의갯수가 전체 길이와 같다면
        return [1,0]
    elif l2 == cnt1: #1의 경우
        return [0,1]
    else: #아니라면 4가지 경우를 끝에서 부터 값을 끌어온다
        t1=QuadComp(ReMake(arr,l//2,l//2,l//2)) #아래 오른쪽
        t2=QuadComp(ReMake(arr,l//2,0,l//2))    #아래 왼쪽
        t3=QuadComp(ReMake(arr,0,l//2,l//2))    #위 오른쪽
        t4=QuadComp(ReMake(arr,0,0,l//2))       #위 왼쪽
        dap=[0,0]
        dap[0]=t1[0]+t2[0]+t3[0]+t4[0]
        dap[1]=t1[1]+t2[1]+t3[1]+t4[1]
        return dap #0의갯수 1의 갯수 카운팅해서 리턴

def solution(arr):
    answer = []
    answer=QuadComp(arr)
    return answer