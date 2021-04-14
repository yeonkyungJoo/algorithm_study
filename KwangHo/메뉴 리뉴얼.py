from itertools import combinations

def solution(orders, course):
    answer = []
    
    arr=[] #조합넣는곳
    brr={} #조합이 몇개 있는지 개수 저장
    crr=[] #2개이상이면서 최대갯수 인것들 추가
    courseMax={}
    for i in range(len(course)): # course의 최대값 넣을 리스트
        courseMax[course[i]] = 0
    
    for i in range(len(course)):
        for j in range(len(orders)):
            arr = list(map(''.join,combinations(orders[j],course[i]))) #2가지 조합
            for k in range(len(arr)):
                temp = ''.join(sorted(list(arr[k]))) #문자열 정렬후
                if brr.get(temp) == None:
                    brr[temp]=0
                brr[temp]+=1 #참조된 조합 증가
                if courseMax[len(temp)] < brr[temp]: #최대참조 구하기
                    courseMax[len(temp)] = brr[temp]
                
    for i in brr.keys():
        if brr[i] >= courseMax[len(i)] and brr[i]>=2 : #brr이 2이상+최대참조라면 crr에 추가
            crr.append(i)
    crr = sorted(crr) #정렬
    
    answer = crr
    return answer