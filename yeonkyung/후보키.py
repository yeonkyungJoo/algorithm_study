def solution(relation):
    row = len(relation)
    col = len(relation[0])
    res = [0] * col
    candidate = []

    def dfs(idx, start, res):

        if idx == col:
            return

        for i in range(start, col):
            res[i] = 1
            tmp = [''] * row
            for j, r in enumerate(res):
                if r == 1:
                    for k in range(row):
                        tmp[k] += relation[k][j]
            if len(tmp) == len(set(tmp)):
                candidate.append(set([idx for idx in range(len(res)) if res[idx] == 1]))
            else:
                dfs(idx+1, i+1, res)
            res[i] = 0

    dfs(0, 0, res)
    candidate.sort(key = lambda x: len(x))
    result = [1] * len(candidate)
    for i in range(len(candidate)):
        for j in range(i+1, len(candidate)):
            if result[j] == 1 and candidate[i].issubset(candidate[j]):
                result[j] = 0
    
    return result.count(1)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    print(solution(relation))
