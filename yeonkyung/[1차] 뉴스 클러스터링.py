def solution(str1, str2):

    str1 = str1.upper()
    str2 = str2.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matrixA = [[0 for _ in range(len(alphabet))] for _ in range(len(alphabet))]
    matrixB = [[0 for _ in range(len(alphabet))] for _ in range(len(alphabet))]
    intersection = []
    union = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            matrixA[ord(str1[i]) - ord('A')][ord(str1[i+1]) - ord('A')] += 1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            matrixB[ord(str2[i]) - ord('A')][ord(str2[i+1]) - ord('A')] += 1

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for _ in range(min(matrixA[i][j], matrixB[i][j])):
                intersection.append(alphabet[i] + alphabet[j])
            for _ in range(max(matrixA[i][j], matrixB[i][j])):
                union.append(alphabet[i] + alphabet[j])

    if len(intersection) == 0 and len(union) == 0:
        answer = 1
    else:
        answer = len(intersection) / len(union)
    return int(answer * 65536)

if __name__ == "__main__":
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"
    print(solution(str1, str2))