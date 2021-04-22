# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
'''
같은 알파벳이 2개 붙어있으면 제거
재귀적으로 반복

input: string (lowercase)
output: int (1 for True, 0 for False)

1 <= len(str) <= 1000000
-> too big to use recursion

should loop at least once?
- sequentially remove
- baabaa -> 1
- ababab -> 0	 

# solution
## stack

stack = [s[0]]  # initial stack value

i = 1
while i < len(s):   # O(n)
	next_char = s[i]
    # if sequential, pop last
	if stack[-1] == next_char:
    	stack.pop()
    else:  # if not sequential, append next char
    	stack.append(next_char)
    i += 1
return 1 if not stack else 0

-> time complexity: O(n)
-> space complexity: O(n)
'''
def solution(s):
    stack = [s[0]]  # initial stack value

    i = 1
    while i < len(s):   # O(n)
        next_char = s[i]
        # if sequential, pop last
        if stack and stack[-1] == next_char:
            stack.pop()
        else:  # if not sequential, append next char
            stack.append(next_char)
        i += 1
    return 1 if not stack else 0
