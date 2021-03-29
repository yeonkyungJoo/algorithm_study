def solution(A,B):
    total = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        total += A[i] * B[i]
    return total

if __name__ == "__main__":
    A = [1, 4, 2]
    B = [5, 4, 4]
    print(solution(A, B))