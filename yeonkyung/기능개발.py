import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    answer = []
    st = days.pop(0)
    count = 1
    while days:
        day = days.pop(0)
        if st >= day:
            count += 1
        else:
            answer.append(count)
            st = day
            count = 1

    answer.append(count)
    return answer

if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))