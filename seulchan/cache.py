# https://programmers.co.kr/learn/courses/30/lessons/17680
# [1차] 캐시
'''

0 <= cacheSize <= 30
cities <= 100000, ignorecase, len(city) <= 20
input: cacheSize(int), cities (list)

LRU
cache hit: 1
cache miss: 5

size = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	
cache [jeju, pangyo, seoul]
time: 5 5 5 1 1 1 1 1 1 => 21

size = 2
["Jeju", "Pangyo", "NewYork", "newyork"]	
cache [ P, N]
size; 5 5 5 1

# solution
## queue -> O(n**2)
if cacheSize == 0: return len(cities) * 5
if not cities: return 0

queue = deque()
answer = 0
for city in cities:  # O(n)
if city in queue:   # O(n)
    answer += 1
else:
	queue.popleft()
    queue.append(city)
    answer += 5

-> time complex: O(n**2)

## can be better than O(n**2)?
# create hash
c = Counter({x:0 for x in s})  # O (n)

for ...: # O(n)
    if c[city]: # get: O(1)
        answer += 1
    else:
        prev = queue.popleft()  # O(1)
        c[prev] -= 1  # O(1)
        queue.append(city)
        answer += 5
        c[city] += 1  # O(1)
        
        
-> time complex O(n) + O(n) => O(n)

-> fail: LRU cache must change order if hit

3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
기댓값 〉	50

cache []
time

'''
from collections import Counter, deque
def solution(cacheSize, cities):
    # solution 1 -> max 60.61ms (test11)
    if not cities: return 0
    if not cacheSize: return 5*len(cities)
    answer = 0
    queue = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            # change hit order to last
            queue.remove(city)
            queue.append(city)
        else:
            queue.append(city)
            answer += 5
    return answer 
    
    # solution 2: using counter to check contains -> 66.60ms로 오히려 오래걸림
    # c = Counter({x.lower():0 for x in cities})
    # queue = deque(maxlen=cacheSize)
    # answer = 0
    # for city in cities:
    #     city = city.lower()
    #     if c[city]:
    #         answer += 1
    #         queue.remove(city)
    #         queue.append(city)
    #     else:
    #         # remove from counter
    #         if queue and len(queue) == cacheSize:
    #             prev = queue[0]
    #             c[prev] = 0
    #         queue.append(city)
    #         c[city] = 1
    #         answer += 5
    # return answer
