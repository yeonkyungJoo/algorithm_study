from itertools import combinations

def solution(info, query):
    answer = []
    
    arr={}
    #정보형태만들기
    for i in info :
        temp=i.split()
        for j in range(1,5):
            key=list(combinations(temp[:4],j))
            for k in key:
                t=''.join(k)
                if arr.get(t):
                    arr[t].append(int(temp[4]))
                else :
                    arr[t]=[]
                    arr[t].append(int(temp[4]))
        if arr.get(''):
            arr[''].append(int(temp[4]))
        else:
            arr['']=[]
            arr[''].append(int(temp[4]))
    
    #정렬
    for i in arr.values():
        i.sort()
    
    #검색
    for i in query:
        key = i.replace(' and ','')
        key = key.replace('-','')
        key = key.split(' ')
        key[1]=int(key[1])
        cnt = 0
        
        if arr.get(key[0]):
            data = arr[key[0]]
            start,end=0,len(data)
            while start!=end and start!=len(data):
                if data[(start+end)//2]>=key[1]:
                    end=(start+end)//2
                else:
                    start=(start+end)//2+1
            answer.append(len(data)-start)
        else :
            answer.append(0)
    return answer

'''
처음에는 경우수마다 돌면서 했는데 효율성에 막힘
딕셔너리로 값추가 해서 검색했는데도 효율성에서 막힘
풀이보니깐 이분검색부분이 효율성에 부딛힌점을 알고 코딩!!
(진짜 생각지도 못한 부분이였음, 데이터가 너누 많으니
이걸 첨부터 끝까지 모든 검사를 실시하니 막히는 부분이였음!)
'''
