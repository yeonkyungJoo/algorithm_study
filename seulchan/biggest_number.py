# https://programmers.co.kr/learn/courses/30/lessons/42746
from collections import queue
# solution 2: time exceeded
def solution(numbers):
    '''
    n >= 0,
    
    2, 20, 23, 32, 3, 4, 9 -> 9433223220
    
    ## solution 1: recursion
    - convert all into string
    - find biggest n[i]
        - if duplicate
        - find n[i+1]
        
    - key: how to solve duplication problem
    - make func for solve_dupliate
   	- duplicate -> find n[i+1]
    original: n[i]
    next: n[i+1]
        if originl < next then added from biggest
        else added origin first and added from biggest
    
    ## solution 2: sort first, and add sequentially / handle duplicated
    - sort: sort from the first index: sort(key=lambda x: x[:], reverse=True)
    - make all to string -> time complexity O(n)
        - but if can solve directly with string, it can be efficient 
    - also have to solve differnt order of number ex. ['34', '30', '3']
    - handle duplicated: tmp_queue
        - tmp_stack -> compare original & next
        - if next is smaller -> it should be back
        - otherwise -> append
        - it has to loop multiple -> too much time complexity
        
    ## solution 3: make all numbers to 4 digits (numbers <= 1000)
    - make all numbers to 4 digit
    - and compare with only one loop
    '''
    answer = ''
    
    # handle duplicated
    def handle_duplicated(duplicated: deque) -> str:
        max_len = max((len(x) for x in duplicated))
        for i, dup in enumerate(duplicated, start=1):
            for i in range(max_len):
                if duplicated[i] > duplicated[i-1]
            
        
    prev = None
    duplicated = queue()
    for x in numbers:
        if x[0] == prev[0]:
            duplicated.append(x)
        else:
            # if duplicated ended, handle it
            if duplicated:
                handle_duplicated(duplicated)
        prev = x
        
    return answer

# solution 3: test case 11이 걸림..
# -> test 11: 모두 0일때는 0000.. 이 아니라 0 반환해야됨!
def solution(numbers):
    '''
    ## solution 3: make all numbers to 4 digits (numbers <= 1000)
    - make all numbers to 4 digit
    - and compare with only one loop
    - return original number and make string
    '''
    # if all is 0, return 0
    if set(numbers) == {0}:
        return '0'
    # make all it to string
    numbers = [(str(x), str(x)*3) for x in numbers]
    
    # sort
    numbers.sort(key=lambda x: x[1][:], reverse=True)
    
    # find original number
    return ''.join((x[0] for x in numbers))
