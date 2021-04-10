# https://programmers.co.kr/learn/courses/30/lessons/42888#
# 오픈채팅방
'''
input: list[Enter/Leave/Change, user_id, nickname]
output: list

change nickname
- leave + enter
- change

# solution; loop once, make dict

loop record
create template
if command is enter:
	append dict if not exist
    change dict if different
    append message (using template)
if command is chagne
	change to dict
if command is leave;
    append message
    
return message from template

-> O(n) + O(n) => O(n)

# 
'''
import string
def solution(record):
    answer = []
    tmps = []
    d = {}
    for r in record:
        command, uid, *nickname = r.split(' ')
        if command in {'Enter', 'Leave'}:
            tmps.append((command, uid))
        if command in {'Enter', 'Change'}:
            d[uid] = nickname[0]
    
    for tmp in tmps:
        if tmp[0] == 'Enter':
            m = f'{d[tmp[1]]}님이 들어왔습니다.'
        else:
            m = f'{d[tmp[1]]}님이 나갔습니다.'
        answer.append(m)
    return answer
           
    # python string.Template 사용시 에러나서 다시
    # 왜 에러나는지 모르겠음
    '''
    answer = []
    d = {}  # user_id: nickname
    for r in record:
        command, uid, *nickname = r.split(' ')
        r = r.split()
        command, uid = r[0], r[1]
        if command in {'Enter', 'Leave'}:
            if command == 'Enter':
                m = f'${uid}님이 들어왔습니다.'
            else:
                m = f'${uid}님이 나갔습니다.'
            answer.append(string.Template(m))
        if command in {'Enter', 'Change'}:
            d[uid] = r[2]
            
    return [x.substitute(d) for x in answer]
    '''
