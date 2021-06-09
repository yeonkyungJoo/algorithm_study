def solution(tickets):
    dic = dict()
    ch = dict()
    for ticket in tickets:
        src, dst = ticket[0], ticket[1]
        if src not in dic:
            dic[src] = []
            ch[src] = []

        dic[src].append(dst)
        ch[src].append(1)

    answer = list()

    def dfs(idx, src, order):

        if src not in dic or 1 not in ch[src]:
            answer.append(order[:])
            return

        for i in range(len(dic[src])):
            if ch[src][i] == 1:
                ch[src][i] = 0
                order.append(dic[src][i])
                dfs(idx + 1, dic[src][i], order)
                order.pop()
                ch[src][i] = 1

    dfs(0, 'ICN', ['ICN'])
    answer.sort(key=lambda x:''.join(x))

    result = answer[0]
    for ans in answer:
        if len(ans) == len(tickets) + 1:
            return ans
    return result

if __name__ == "__main__":
    tickets =  [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
    print(solution(tickets))