'''
input: int, list (words)
output: list (fail, order)

2 <= n <= 10
n <= words <= 100
2 <= word <= 50
[0,0] if no one drops

-> check duplication, valid words

# solution
## find invalid word -> find order

## find invalid word + counting result

order = 1
count = 0
current = []
for i, word in enumerate(words):  # O(n)
	# order update (현재 순서)
	if order == n:
    	order = 1
    else:
    	order += 1
    # check duplication, valid word
	if word in current:  # O(n)
        count = math.ceil(i/n)
    	break
    if word[0] != current[-1][-1]:
        count = math.ceil(i/n)
    	break
if not current: return [0, 0]	
	else: [order, count]
    
-> O(n**2)
-> can find better? change current from list to dict
'''
import math
def solution(n, words):
    order = 0
    count = 0
    current = []
    for i, word in enumerate(words, start=1):  # O(n)
        # order update (현재 순서)
        if order == n:
            order = 1
        else:
            order += 1
        # check duplication, valid word
        if word in current or (current and word[0] != current[-1][-1]):  # O(n)
            count = math.ceil(i/n)
            break
        current.append(word)
    if not count:
        return [0, 0]	
    return [order, count]

# 좋은풀이: 시간복잡도는 비슷하지만 따로 비교할 리스트를 만들지 않아서 공간복잡도가 O(1)
def solution(n, math):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p%n)+1, (p//n)+1]
        else:
            return [0,0]
