def solution(people, limit):
    people = sorted(people, reverse=True)

    if len(people) == 1:
        return 1

    count = 0
    l, r = 0, len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1
        count += 1
    return count

if __name__ == "__main__":
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit))

'''
def solution(people, limit):
    people = sorted(people, reverse=True)

    count = 0
    while people:
        if len(people) == 1:
            count += 1
            break
        else:
            if people[0] + people[-1] <= limit:
                people.pop(0)
                people.pop()
            else:
                people.pop(0)
            count += 1
    return count
'''