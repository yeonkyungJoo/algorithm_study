def solution(m, musicinfos):
    answer = '(None)'
    max = 0
    # 이게 A# A가 겹치는거때문에 아예 다른 숫자로
    m=m.replace('A#','O')
    m=m.replace('C#','P')
    m=m.replace('D#','Q')
    m=m.replace('F#','R')
    m=m.replace('G#','S')

    for i in musicinfos:
        arr=i.split(',') #4개로나눈다음에
        
        arr[3]=arr[3].replace('A#','O')
        arr[3]=arr[3].replace('C#','P')
        arr[3]=arr[3].replace('D#','Q')
        arr[3]=arr[3].replace('F#','R')
        arr[3]=arr[3].replace('G#','S')
        
        t1,t2=arr[0].split(':')
        t3,t4=arr[1].split(':')
        t1 = int(t1)
        t2 = int(t2)
        t3 = int(t3)
        t4 = int(t4)
        
        s1 = t1*60+t2
        s2 = t3*60+t4

        d = s2-s1 #재생길이 구하고
        if d < 0 : #24시면 0이라서 -나올면 x-1
            d *= -1
        
        #재생길이까지 노래길이 맞쳐준다.
        arrL = len(arr[3])
        if d%arrL==0 :
            arr[3] = arr[3]*(int(d/arrL))
        else :
            arr[3] = arr[3]*(int(d/arrL)) + arr[3][:int(d%arrL)]

        # 음악이 포함되어있고 + 가장큰길이라면 OK
        if m in arr[3] and d > max :
            answer = arr[2]
            max = d
    
    return answer