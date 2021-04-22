# https://programmers.co.kr/learn/courses/30/lessons/68936
# 쿼드압축 후 개수 세기
'''
input: 2x2 array
output: array (count 0, 1)

[
[1, 1, 0, 0],
[1, 0, 0, 0],
[1, 0, 0, 1],
[1, 1, 1, 1]
]

combination of num 
row: 0, 1  /  2, 3
col: 0, 1  /  2, 3

# solution - recursion
## pseudocode
answer = [0, 0]
len_arr = len(arr)
	
def compression(x, y, n):
	original = arr[x][y]
    for i in range(x, x+n):
    	for j in range(x, y+n):
        	if arr[i][j] != original:
            	next_n = n / 2
                compression(x, y, next_n)
                compression(x+n, y, next_n)
                compression(x+n, y+n, next_n)
                compression(x, y+n, next_n)
	answer[original] += 1
compression(0, 0, len_arr)
'''
def solution(arr):
    answer = [0, 0]
    len_arr = len(arr)

    def compression(x, y, n):
        original = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != original:
                    next_n = n // 2
                    compression(x, y, next_n)
                    compression(x+next_n, y, next_n)
                    compression(x+next_n, y+next_n, next_n)
                    compression(x, y+next_n, next_n)
                    return
        answer[original] += 1
    compression(0, 0, len_arr)
    return answer
