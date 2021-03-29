# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def solution(numbers):
    '''
    # pre-settings
    len(numbers): 1 ~ 7 -> maximum 7! (5000)
    
    # solution
    ## 1. make all possible number and check is_prime
    - can make maximum n! num
    - time-complexity: O(n!) -> it's ok because max is 7!
    - key: 
        - how to make all possible numbers -> itertools.combinations
        - how to check is_prime
    
    ## 2. pre-determine from the first digits
    - a: check if x is prime number
    - ba: use only a
    '''
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
        
    # solution 1
    possible = []
    for i in range(len(numbers)):
        comb = permutations(numbers, i+1)
        for x in set(comb):
            possible.append(int(''.join(x)))
        
    return sum([is_prime(x) for x in set(possible)])
