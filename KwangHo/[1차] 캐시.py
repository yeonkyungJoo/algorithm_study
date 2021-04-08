def solution(cacheSize, cities):
    answer = 0
    arr=[]
    d=0
    for i in cities:
        i = i.upper()
        if i in arr :             #캐쉬히트
            d+=1
            arr.pop(arr.index(i)) #위치찾아서 팝
            arr.append(i)         #맨뒤에 추가
        else :                    #캐쉬미스   
            d+=5

            if cacheSize == 0 : continue    #캐쉬길이0예외처리
            if cacheSize == len(arr):       #옛날꺼 팝
                arr.pop(0)
            arr.append(i)                   #최근꺼 추가
            
    answer = d
    return answer