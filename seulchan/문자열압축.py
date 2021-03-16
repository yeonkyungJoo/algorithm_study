def solution(s):
    # for문을 돌면서 매칭되는 글자 찾기
    # -> 이 방법으로는 언제 매칭되는지 알기 힘듬
    # is_palindrome을 써야됨
    # 찾으면 list에 더하기
    # 글자수 분류
    # 더 효율적인 글자수 찾기 -> 어떻게?
        
    # 방법2
    # x단위로 잘리는지 확인 후
    # 잘리면 해당 개수 확인 후 저장
    # 안잘리면 return len(s)
    def cutted(num):
        i = 0
        zip_list = []
        while True:
            if i+num > len(s):
                zip_list.append(s[i:])
                break
            else:
                zip_list.append(s[i:i+num])
            i = i+num

        my_zip = ""
        before = zip_list[0]
        count = 1
        for i in range(1, len(zip_list)):
            curr = zip_list[i]
            if curr == before:
                count += 1
            else:
                if count == 1:
                    my_zip = my_zip + before
                else:
                    my_zip = my_zip + str(count) + before
                count = 1
            before = curr
        my_zip = my_zip + before
        return len(my_zip)
    
    def can_cutted(x: int) -> str:
        # x가 2라면 s[:2] == s[2:4] == s[4:6] 이런식으로 비교
        first = s[0:i]
        matched_count = 1
        for i in range(x, len(s), x):
            if s[i:i+x] == first:
                matched_count += 1
                continue
            if matched_count > 1:
                dap += str(matched_count)
            dap += temp
            temp = s[i:i+1]
            matched_count = 1
        return dap
            
        s[:x] == s[x:x+x]
        s[:2] == s[2:4]
        s[4:6] == s[6:8]
        
    return_length = len(s)
    temp = 0
    for i in range(1, len(s)//2 + 1):
        temp = cutted(i)
        if temp < return_length:
            return_length = temp
    return return_length

