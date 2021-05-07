def convert(music):
    converted = []
    for idx, ch in enumerate(music):
        if ch == '#':
            converted[-1] = converted[-1].lower()
        else:
            converted.append(ch)
    return ''.join(converted)

def solution(m, musicinfos):
    answer = []

    for musicinfo in musicinfos:
        info = musicinfo.split(",")
        start, end, title = info[0], info[1], info[2]
        music = convert(info[3])
        m = convert(m)

        length = len(music)
        start_minutes = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
        end_minutes = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
        minutes = end_minutes - start_minutes

        if minutes > length:
            total = music * (minutes // length) + music[:minutes % length]
        else:
            total = music[:minutes]

        if total.find(m) > -1:
            answer.append((title, minutes))

    if not answer:
        return "(None)"
    else:
        answer.sort(key=lambda x : -x[1])
        return answer[0][0]

if __name__ == "__main__":
    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    print(solution(m, musicinfos))
