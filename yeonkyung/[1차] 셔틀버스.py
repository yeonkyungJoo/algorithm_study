def change(time):
    tmp = time.split(":")
    return int(tmp[0]) * 60 + int(tmp[1])

def solution(n, t, m, timetable):
    bus = []
    start = change("09:00")
    for _ in range(n):
        bus.append(start)
        start = start + t

    re = []
    for time in timetable:
        re.append(change(time))
    re.sort(reverse=True)

    for i in range(len(bus)-1):
        for _ in range(m):
            if re[-1] <= bus[i]:
                re.pop()

    re = [r for r in re if r <= bus[-1]]
    re.sort()
    if len(re) < m:
        answer = bus[-1]
    elif len(re) == m:
        answer = re[-1]-1
    else:
        answer = re[m-1]-1

    hour = answer // 60
    minute = answer % 60
    return ("0" + str(hour) if hour < 10 else str(hour)) + ":" + ("0" + str(minute) if minute < 10 else str(minute))

if __name__ == "__main__":
    n, t, m = 10, 60, 45
    timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, timetable))