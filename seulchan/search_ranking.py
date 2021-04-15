'''
info: ["python backend senior chicken 100000"...]
1 <= len(info) <= 50000

query: ["java and backend and senior and pizza 100"]
- ["con1 and con2 and con3 and con4 score", ...]
- condition can be none -> "-"
- score 이상 받은 사람 count
1 <= len(query) <= 100000

input: array (info), array (query)
output: array (count of people)

# solution
- data structure? hash (dict) ? B-tree ?
    - 매 쿼리마다 for loop 필요 -> O(n)
    - query 개수만큼 for -> O(n)
    - add ascending of score -> can save time?
{
	language: python,
    job: backend,
    career: junior,
    food: chicken
    score: 100,
}
## 1) or make only key -> O(1)
{
    java:1,
    backend:1,
    senior:1,
    pizza:1,
    score:105,
}
## 2) brute force? + save result

loop info
	loop query
    	add result

## pseudocode of 1)

# sort info from score  # O(nlogn)
info.sort(key=lambda x: x.split(' ')[-1])

new_info = []
for inf in info:
    d = dict()  # can save order
    for x in inf.split(' '):
    	d[x] = 1
    new_info.append(d)

# loop query
answer = []
for q in query:
	lang, job, career, food = q.split(' and ')
    food, score = food.split(' ')
    
	# query
    count = 0
    for inf in new_info:
        # break if lower score
    	if inf[score] < score:
            break
            
        if lang == '-' or lang not in inf:
            continue
        if job == '-' or job not in inf:
            continue
        if career == '-' or career not in inf:
            continue
        if food == '-' or food not in inf:
            continue
        count += 1
return answer	
'''
def solution(info, query):
    # sort first: O(nlogn)
    info.sort(key=lambda x: int(x.split(' ')[-1]), reverse=True)

    new_info = []
    for inf in info:  # O(n)
        d = dict()  # can save order
        for i, x in enumerate(inf.split(' ')):  # O(n)
            d[x] = 1
            if i == 4:
                d['score'] = int(x)
        new_info.append(d)


    # loop query
    answer = []
    for q in query:
        lang, job, career, food = q.split(' and ')
        food, score = food.split(' ')

        # query
        count = 0
        for inf in new_info:
            # break if lower score
            if inf['score'] < int(score):
                break

            if lang != '-' and lang not in inf:
                continue
            if job != '-' and job not in inf:
                continue
            if career != '-' and career not in inf:
                continue
            if food != '-' and food not in inf:
                continue
            count += 1
        answer.append(count)
    return answer


'''
효율성 테스트 실패. for문이 중첩되어서 그런듯
'''
