import random
import timeit

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
# 횟수 수정
TOTAL_COUNTS = 5

# functions
myfunction = '''
def solution(files):
    def sortFunc(x: str) -> tuple:
        head, number, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', x)[0]
        return (head.lower(), int(number))
    
    return sorted(files, key=sortFunc)
solution(numbers)
'''

for trial in [2**_ for _ in range(1, TOTAL_COUNTS)]:
    # 문제에 맞게 수정
    numbers = [f'{random.choice(WORDS)}{random.randint(0, 99999)}' for _ in range(trial)]
    WORDS = open(word_file).read().splitlines()
    m = timeit.timeit(stmt=myfunction, globals={
        'numbers': numbers,
    })
    print('{0:d} {1:f}'.format(trial, m)) 


# 단순 순자 사용할경우
myfunction = '''
for i in range(len(numbers)):
    continue
'''
for trial in [2**_ for _ in range(1, TOTAL_COUNTS)]:
    numbers = [random.randint(1, 9) for _ in range(trial)]
    m = timeit.timeit(stmt=myfunction, globals={
        'numbers': numbers,
    })
    print('{0:d} {1:f}'.format(trial, m)) 
    


'''
O(n**2): size is double, time is multiply factor 4
O(n): size is double, time is double
'''
