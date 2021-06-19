def solution(A, B):
    score = 0

    A.sort()
    B.sort()

    i, j = 0, 0
    while j < len(B):
        a = A[i]
        b = B[j]
        if b > a:
            score += 1
            i += 1
            j += 1
        else:
            j += 1

    return score


if __name__ == "__main__":
    A = [2,2,2,2]
    B = [1,1,1,1]
    print(solution(A, B))