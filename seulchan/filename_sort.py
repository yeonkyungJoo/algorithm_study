# https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일명 정렬
'''
sort: string -> consider integer
filename: < 100, a-z,A-Z,\d,\s,.,-
strats with a-z, including at least 1 int
- head; all string, at least 1
- number: 1 ~ 5, 00000 ~ 99999 (start from zero possible)
- tail; rest of them: can be empty

sort
- head: ignore case
- number: ignore 0 prefix, 012 == 12
- if head+number order same, remaining order: MUZI01.zip, muzi1.png

input: array, len(files) <= 1000, unique, 
output; sorted array

# solution
- already sorted with filename -> bubble sort

## 1. use python sort with key
def sortFunc(x):
    # divide head, number, tail
    # regex
    # ([a-zA-Z]+)
    # (\d{1,5})
    # (.?)
    head, number, _ = re.findall('([a-zA-Z]+)(\d{1,5})(.?)', x)  # O(n)
    return (head, number)

return sorted(files, key=sortFunc)  # O(nlogN)
- time complex: O(n) + O(nlogN) = O(n)
- space complex: O(n)

["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
img1.png, img01.gif

## 2. buble sort -> max O(n**2)

def compare(x, y) -> list:
    xhead, xnumber, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', x)[0]
    yhead, ynumber, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', y)[0]
    heads = [xhead, yhead]
    numbers = [xnumber, ynumber]
    sorted(heads)
    if heads[1] == yhead:
        return [y, x]
    sorted(numbers)
    if numbers[1] == ynumber:
        return [y, x]
    return [x, y]

for size in reversed(range(len(files))):
    for i in range(size):
        # compare
        x[i], x[i+1] = compare(x[i], x[i+1])
    

'''
# solution 2
import re
def solution(files):
    def compare(x, y) -> list:
        xhead, xnumber, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', x)[0]
        yhead, ynumber, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', y)[0]
        heads = [xhead, yhead]
        numbers = [int(xnumber), int(ynumber)]
        sorted(heads)
        if heads[1] == yhead:
            return [y, x]
        sorted(numbers)
        if numbers[1] == int(ynumber):
            return [y, x]
        return [x, y]

    for size in reversed(range(len(files))):
        for i in range(size):
            # compare
            files[i], files[i+1] = compare(files[i], files[i+1])
    return files
    
# solution 1
import re

def solution(files):
    def sortFunc(x: str) -> tuple:
        head, number, _ = re.findall('([a-zA-Z\s\.\-]+)(\d{1,5})(.?)', x)[0]
        return (head.lower(), int(number))
    
    return sorted(files, key=sortFunc)

'''
# 1번으로 풀려고 했는데 제출시 기존 순서를 바꿔버리는 문제 발생
-> python 내장 sort는 기존 순서를 유지한다. (정렬 안정성)
-> lower()를 했어야하는데 하지 않아서 생긴 문제
# 1번으로 안풀려서 2번 bubble sort를 쓰려고 했는데 30분 시간이 끝남. 정렬 공부를 더 해야할듯

1. time complexity
- regex 사용: O(n)
- 내장 sort를 사용하여 O(nlogn)
- sort에 key를 두개 사용하면 O(n**2)이 되는게 아닌가? 이부분은 확인해봐야될듯
-> O(n) time complexity가 나온다
internal
2 3.515740
4 6.337292
8 12.348596
16 24.354847
'''
