def solution(s):
    min_len = len(s)

    # 문자열의 절반까지만 확인하면 된다.
    for l in range(1, len(s)//2+1):
        count = []

        i = 0
        tmp, cnt = None, 0
        while i < len(s):
            # 가장 최근 문자 (s[-1])을 tmp로 두고 비교
            # 맨 처음에는 tmp가 없다.
            if tmp is None:
                tmp = s[i:i+l]
                cnt = 1
            else:
                # tmp가 존재하는 경우
                # 즉 이전 문자와 비교
                if s[i:i+l] == tmp:
                    cnt += 1
                else:
                    # 1은 삽입 X
                    if cnt != 1:
                        count.append(str(cnt))
                    count.append(tmp)
                    tmp = s[i:i+l]
                    cnt = 1

            i += l

        # 1은 삽입 X
        if cnt != 1:
            count.append(str(cnt))
        count.append(tmp)

        #print(''.join(count))
        min_len = min(min_len, len(''.join(count)))
    return min_len

if __name__ == "__main__":
    s = 'xababcdcdababcdcd'
    print(solution(s))