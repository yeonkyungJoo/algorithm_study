def solution(record):
    answer = []
    nickname = dict()

    for text in record:
        split = text.split(" ")
        verb, id = split[0], split[1]
        if verb == "Enter" or verb == "Change":
            nickname[id] = split[2]

    for text in record:
        split = text.split(" ")
        verb, id = split[0], split[1]

        if verb == "Enter":
            answer.append(nickname[id] + "님이 들어왔습니다.")
        elif verb == "Leave":
            answer.append(nickname[id] + "님이 나갔습니다.")

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))