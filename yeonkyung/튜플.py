def solution(s):

    s = s[2:-2].split("},{")
    s = sorted(s, key=lambda x:len(x))

    answer = []
    tmp = {}
    for nums in s:
        curr = set(nums.split(","))
        answer.append(int((curr - set(tmp)).pop()))
        tmp = curr
    return answer

if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))