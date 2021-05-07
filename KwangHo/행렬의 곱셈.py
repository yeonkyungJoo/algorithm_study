def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        answer.append([0]*len(arr2[0]))
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    return answer
'''
ij    ik   kj
00 += 00 x 00
00 += 01 x 10
00 += 02 x 20

01 += 00 x 01
01 += 01 x 11
01 += 02 x 21

01 += 00 x 02
01 += 01 x 12
01 += 02 x 22

행렬
n x m , m x l
=> n l로 나옴
'''