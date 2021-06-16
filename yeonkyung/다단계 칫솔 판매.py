def solution(enroll, referral, seller, amount):
    answer = dict()
    ref = dict()
    for i, en in enumerate(enroll):
        answer[en] = 0
        ref[en] = referral[i]
    # print(ref)

    for idx, person in enumerate(seller):
        p = person
        price = amount[idx] * 100
        while True:
            if p == '-':
                break

            if int(price * 0.1) != 0:
                ten = int(price * 0.1)
                answer[p] += price - ten
                price = ten
                p = ref[p]
            else:
                answer[p] += price
                break

    return list(answer.values())


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["sam", "emily", "jaimie", "edward"]
    amount = [2, 3, 5, 4]
    print(solution(enroll, referral, seller, amount))