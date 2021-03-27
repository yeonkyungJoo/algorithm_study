def solution(number, k):
    answer = ''
    arr = []
    
    for i in range(len(number)):
        arr.append(int(number[i])) #숫자로 바꿔주고
    
    idx = -1
    for i in range(0,len(arr)-k): #0부터 k뺴고 자리수까지
        max = 0
        
        for j in range(idx+1,i+k+1): # 0~k까지  그담은 max , 인덱스 부터 k-1까지
            if max < arr[j] :
                max = arr[j]
                idx = j
                if max == 9 : # max가 9라면 최고 큰수니깐 비교필요x
                    break
        answer += str(max)
    
    return answer

'''
방식을 이리 저리 실험 해보다가

1. 앞에서 k만큼 돌려서 최고의수를 찾고
2. 최고의수 기준으로 앞에서 k-1만큼 찾는다 ( 하나 찾았으니깐)
3. 또 최고의 수 기준으로 앞에서부터 k-2만큼 찾는다.

이렇게 잘풀었는데 자꾸 시간초과가 나서 시간 또 끌다가
k자리수가 엄청 길기에 max가 9라면 찾지 않아도 되니깐 탈출
(이 부분은 질답을 통해 답변을 얻었다.) : 당연한걸 생각 못햇다.
자리수가 얼마나 크겟어 했는데 백만자리라늬;;;;(입출력 크기 확인 잘하자)
'''