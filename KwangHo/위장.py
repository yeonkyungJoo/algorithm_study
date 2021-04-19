def solution(clothes):
    answer = 1
    arr={}
    
    for i in clothes:
        if not i[1] in arr:
            arr[i[1]]=[]             
        arr[i[1]].append(i[0])

    for i in arr.values():
        answer *= (len(i)+1)
    answer -=1
    return answer
'''
딕셔녀리로 부위별 카운트

딕셔버리 벨류 돌면서
갯수+안입는거1 해서 곱해주면
경우의 수 체크
예시1번은
2+1 * 1+1 = 6
둘다안입을 경우 -1 해서 5
'''