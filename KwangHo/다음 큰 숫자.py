def solution(n):
    answer = 0  
    arr=[]

    while n!=1: # 2진수 값 만들기
        na = int(n%2)
        arr.insert(0,na)
        n = int(n/2)
    arr.insert(0,1)
    
    if arr.count(1) == len(arr): #1카운트==전체길이
        arr.insert(1,0)          #가장은수는 2번째 자리에 0추가
    else :
        c = arr.count(1) # 현재 1의 개수 카운트
        while True :     # +1씩 하면서 1카운트 개수 맞늦지 체크
            arr[len(arr)-1] += 1
            for i in range(len(arr)-1,0,-1) :
                if arr[i] == 2 :
                    arr[i] = 0
                    arr[i-1]+=1
                    
            if arr[0] == 2 :
                arr[0] = 0
                arr.insert(0,1)

            if c == arr.count(1) :
                break
            

    t=0
    for i in range(len(arr)-1,-1,-1): #풀어쓰기
        answer += 2**t * arr[i]
        t+=1
    
    return answer

'''
1. 2진수로 풀어낸다음
2. 1의 카운트 비교해서 전체길이랑 같으면 2번에 0추가
   아니면 +1씩하면서 1의 카운트 수와 맞는걸 체크
3. 10진수로 풀어냄
'''