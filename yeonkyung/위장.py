'''
from itertools import combinations
def solution(clothes):
    count = 0
    clothes_dict = dict()
    for e in clothes:
        if e[1] not in clothes_dict:
            clothes_dict[e[1]] = 0
        clothes_dict[e[1]] += 1

    for i in range(1, len(clothes_dict) + 1):
        combi_list = list(combinations(clothes_dict.values(), i))
        # print(combi_list)
        for combi in combi_list:
            tmp = 1
            for j in combi:
                tmp *= j
            count += tmp
    return count
'''

def solution(clothes):
    count = 0
    clothes_dict = dict()
    for e in clothes:
        if e[1] not in clothes_dict:
            clothes_dict[e[1]] = 0
        clothes_dict[e[1]] += 1
        count += 1

    if len(clothes_dict) == 1:
        return count
    else:
        tmp = 1
        for v in clothes_dict.values():
            tmp *= (v+1)
        return tmp - 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))