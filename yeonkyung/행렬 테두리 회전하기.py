def solution(rows, columns, queries):
    matrix = [[ columns * i + j for j in range(1, columns+1)] for i in range(rows)]
    result = []
    for query in queries:
        arr = []
        start = query[0]-1, query[1]-1
        end = query[2]-1, query[3]-1

        x, y = start[0], start[1]
        tmp = matrix[x][y]
        for y in range(start[1]+1, end[1]+1):
            v = matrix[x][y]
            arr.append(v)
            matrix[x][y] = tmp
            tmp = v

        for x in range(start[0]+1, end[0]+1):
            v = matrix[x][y]
            arr.append(v)
            matrix[x][y] = tmp
            tmp = v

        for y in range(end[1]-1, start[1]-1, -1):
            v = matrix[x][y]
            arr.append(v)
            matrix[x][y] = tmp
            tmp = v

        for x in range(end[0]-1, start[0]-1, -1):
            v = matrix[x][y]
            arr.append(v)
            matrix[x][y] = tmp
            tmp = v

        result.append(min(arr))

    return result

if __name__ == "__main__":
    rows, columns = 100, 97
    queries = [[1,1,100,97]]

    print(solution(rows, columns, queries))