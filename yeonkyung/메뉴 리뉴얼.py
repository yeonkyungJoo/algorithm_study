from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:
        course_dict = dict()

        for order in orders:
            if len(order) < 2:
                continue

            combs = list(combinations(order, num))
            combs_list = [''.join(comb) for comb in combs]
            for combs in combs_list:
                combs = ''.join(sorted(list(combs)))
                if combs not in course_dict:
                    course_dict[combs] = 1
                else:
                    course_dict[combs] += 1

        tmp = []
        max_value = -1
        for item in course_dict.items():

            if item[1] < 2:
                continue

            if max_value < item[1]:
                tmp.clear()
                tmp.append(item[0])
                max_value = item[1]
            elif max_value == item[1]:
                tmp.append(item[0])

        answer.extend(tmp)

    return sorted(answer)

if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    print(solution(orders, course))