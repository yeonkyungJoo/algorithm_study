# https://programmers.co.kr/learn/courses/30/lessons/42883
# solution 2: O(n**2)이 나와서 time exceed
def solution(number, k):
    '''
    # Pre-communication
    data structure -> many numbers? or big numbers
    
    # solutions
    ## solution 1: remove from first + the rest
    - result: (number - k) digits
    - remove from first -> compare only in number[:k-1] / number[k]
        - if number[k] is bigger than number[:k-1] then remove number[:k-1]
        - else then find biggest number in number[:k-1]
        - set first number for the biggest and remove rest from left (and count++)
    - remove the rest (k-count)
        - find downgrade num: if number is start smaller -> remove the smaller number
    
    -> time complex: O(n), space complex: O(k)?
    -> too many if/else condition
    
    ## solution 2: remove only one + recursion
    - it's same for removing one repeately
    - key: how to find removing element?
        - find element when rising (element smaller than next)
        - what if nothing rising? (9876) -> remove last
    
    -> time complex: O(n**2), space complex: high if not use callstack
    -> have to find way with only one loop
    
    ## solution 3
    
    # post-communiation
    '''
    answer = ''
    # if all descending
    if sorted(number, reverse=True) == list(number):
        return number[:len(number)-k]
    
    for i in range(k):
        tmp_num = number
        # should find other way than for loop
        for i, num in enumerate(tmp_num[:-1]):
            # if next one is bigger
            if int(num) < int(tmp_num[i+1]):
                # remove number[i]
                number = tmp_num[:i] + tmp_num[i+1:]
                break
    
    return number

