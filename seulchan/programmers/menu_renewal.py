# https://programmers.co.kr/learn/courses/30/lessons/7241://programmers.co.kr/learn/courses/30/lessons/72411 
# 메뉴 리뉴얼
'''
input: orders(list), course(list)

- at least 2 menu, at least 2 order

# solution
## brute force
- make all combination from course (len)
- filter combination
    - at least 2
    
combis = []
for c in course:
	for order in orders:
    	# create combination
        combis.extend(list(combinations(order, c)))
# filter combinations
counter = Counter(combis)
return [x for x in counter if counter[x] in set(course)]

-> should ignore order of orders
'''
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        course_answer = []
        for order in orders:
            course_answer.extend([''.join(sorted(x)) for x in list(combinations(order, c))])
        if not course_answer:
            continue
        counter = Counter(course_answer).most_common()
        # find most common
        most_common = counter[0][1]
        for x, count in counter:
            if count == most_common and count > 1:
                answer.append(x)
    return sorted(answer)

'''
combinations, counter로 쉽게 풀었지만 라이브러리 없이 푸는 방법을 연습해봐야할듯.
itertools 문서도 시간날때마다 확인하자
'''
