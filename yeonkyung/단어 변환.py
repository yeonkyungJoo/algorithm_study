def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    ch = [0 for _ in range(len(words))]

    def dfs(idx, cur):
        nonlocal answer

        if cur == target:
            answer = idx
            return

        if idx == len(words):
            return

        for i, word in enumerate(words):
            if ch[i] == 0:

                cnt = 0
                for j in range(len(cur)):
                    if word[j] != cur[j]:
                        cnt += 1

                if cnt == 1:
                    ch[i] = 1
                    dfs(idx + 1, word)
                    ch[i] = 0

    dfs(0, begin)
    return answer


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))