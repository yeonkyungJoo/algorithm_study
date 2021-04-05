import operator

def solution(files):
    answer = []
    arr={}
    
    #풀기
    for i in files:
        Head = ''
        Number = ''
        Tail = ''
        for j in range(len(i)):      # 1. Head와 나머지를 임시로 Number에 넣기
            if i[j] in "0123456789":
                Head = i[:j]
                Number = i[j:]
                break
        for j in range(len(Number)): # 2. 임시Number을 Number와 Tail에 나눠 넣기
            if not Number[j] in "0123456789":
                Tail = Number[j:]
                Number = Number[:j]
                break
        
        h = Head.upper() #대문자통일
        n = int(Number)  #숫자로
        v = []           #리스트만들어서
        v.append(h)
        v.append(n)
        arr[i]=v         # Key:원본 문자열 , Value: Head,Number리스트로 넣기
        
    #정렬후    
    arr = sorted(arr.items(),key=operator.itemgetter(1)) #리스트값 기준 정렬
    brr = []
    
    #출력형식
    for i in arr:
        brr.append(i[0])
    
    answer = brr
    return answer