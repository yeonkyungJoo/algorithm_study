# https://programmers.co.kr/learn/courses/30/lessons/17684
# [3차] 압축
'''
LZW
dict = {
1: A
2: B
3: C
...
26: Z
27: KA
}

KAKAO
1) K -> KA / 11 / 27: KA
2) A -> AK / 1 / 28: AK
3) K -> KA -> KAO / 27 / 29: KAO

input: sequence character of msg
output: the index of input

# sequentially check
dic = dict(1='A', 2='B', 3='C', ...)
answer = []
for i in range(len(msg)):
    x = i
    result = msg[i]
    while not msg[x]:
        x += 1
        result += msg[x]
    answer.append(x)
    dic[len(dic)+1] = result

# example
KAKAO

i = x = 0
    result = K
    x += 1
    ---
    x = 1
    reulst = KA
    ---
    dic[27] = KA

i = x = 1
	result = A
    x += 1
    ---
    x = 1
    result = AK
    ---
    dic[28] = AK
i = x = 2
	result = K
    x += 1
    ---
    x = 1
    result = KA
    x += 1
    ---
    x = 2
    result = KAO
    ---
    dic[29] = KAO
'''
# 시간복잡도 통과 못함
def solution(msg):
    # 반대로 만들어야 편리함
    reverse_dic = dict(
       (x, i) for i, x in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)
    )
    
    i = 0
    answer = []
    while i < len(msg):
        j = i
        keys = reverse_dic.keys()
        while msg[i:j+1] in keys and j < len(msg):
            j += 1
            
        if j == len(msg):
            break
            
        finded = msg[i:j]
        added = msg[i:j+1]
        answer.append(reverse_dic[finded])
        reverse_dic[added] = len(reverse_dic) + 1
        i = j
        
    answer.append(reverse_dic[msg[i:j]])
    return answer
