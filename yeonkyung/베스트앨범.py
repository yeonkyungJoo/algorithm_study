def solution(genres, plays):
    answer = []

    dic = dict()
    for i, genre in enumerate(genres):
        if genre not in dic:
            dic[genre] = [0, []]

        dic[genre][0] += plays[i]
        dic[genre][1].append((i, plays[i]))

    tmp = []
    for k, v in dic.items():
        v[1].sort(key=lambda x: (-x[1], x[0]))
        tmp.append(v)

    tmp.sort(key=lambda x: -x[0])
    for i in range(len(tmp)):

        order = tmp[i][1]
        if len(order) > 2:
            for j in range(2):
                answer.append(order[j][0])
        else:
            for j in range(len(order)):
                answer.append(order[j][0])

    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))