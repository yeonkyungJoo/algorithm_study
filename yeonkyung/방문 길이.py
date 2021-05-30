def solution(dirs):
    graph = [[1 for _ in range(-10, 11)] for _ in range(-10, 11)]
    direction = {
        "U" : (0, 2),
        "D" : (0, -2),
        "R" : (2, 0),
        "L" : (-2, 0)
    }

    count = 0

    x, y = 0, 0
    for dir in dirs:
        xx = x + direction[dir][0]
        yy = y + direction[dir][1]

        if -10 <= xx <= 10 and -10 <= yy <= 10:
            if graph[int((x+xx)//2)][int((y+yy)//2)] == 1:
                count += 1
                graph[int((x + xx) // 2)][int((y + yy) // 2)] = 0

            x = xx
            y = yy

    return count

if __name__ == "__main__":
    dirs = "ULURRDLLU"
    print(solution(dirs))