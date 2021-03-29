def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer

'''
최소값을 만들기 위해서는
오름차순 x 내림차순
'''