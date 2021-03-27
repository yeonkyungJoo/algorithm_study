def solution(numbers):
    answer = ""
    
    arr=[]
    for i in numbers:
        #t1 = ""
        #t2 = ""
        t1 = str(i) #원본
        t2 = str(i) #복사본
        #print(t1[0])
        #print(t2,t2)
        j = 0
        #print(len(t2))ㄴ
        #print(t2 + t1[0])
        while True:  # 1자리,2자리,3자리는 4자리로 다 가득 채우기
            t2 += t1[j]
            j = (j+1) % len(t1)
            if len(t2) >= 4 :
                break
            
        arr.append([t2,t1])
    
    arr = sorted(arr,reverse=True) #정렬
    #print(arr)
    answer = ''.join(i[1] for i in arr) #이번에 배웠다 join
    if answer[0]=='0': # 0 예외처리
        answer = '0'
    return answer

'''
1자리 2자리 3자리 4자리 케이스는 빨리 찾았는데(처음에 소수4자리로 하다가 피봣다)
와우 , 0,0,0,0케이스를 생각 봇해서 시간이 너무 오래결렸다.
그리고 원래는 숫자배열 + 체크배열 2개로 그냥 일반 정렬로
짜서 했는데 시간초과 나서 내장함수로 돌리니 시간초과는 없었다.
아 그리고 리스트에 리스트를 넣는 걸 몰라서 내장함수 정렬 돌리면
어떻게 체크 할지 때문에 처음엔 딕셔너리로 했다가 어차피
별반 다를게 없는거 떔에 , 여러무로 삽질을 많이해서 3시간은 걸린것 같다ㅠ
'''