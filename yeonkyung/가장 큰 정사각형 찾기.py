def solution(board):

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] >= 1:
                if board[i-1][j] >= 1 and board[i][j-1] >= 1 and board[i-1][j-1] >= 1:
                    board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            answer = max(answer, board[i][j])

    return answer ** 2

if __name__ == "__main__":
    board = [[0]]
    print(solution(board))
