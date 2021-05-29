from itertools import permutations
import sys

def split(expression):

    oper = []
    nums = []
    tmp = 0
    for i in range(len(expression)):
        if expression[i] in ['-', '*', '+']:
            oper.append(expression[i])
            nums.append(int(expression[tmp:i]))
            tmp = i+1
    nums.append(int(expression[tmp:]))

    result = [nums[0]]
    for i in range(len(oper)):
        result.append(oper[i])
        result.append(nums[i+1])
    return oper, result

def solution(expression):

    oper, exp = split(expression)
    orders = list(set(oper))
    # print(oper, exp, orders)

    answer = -sys.maxsize
    for order in list(permutations(orders)):
        ex = exp
        for op in order:
            stack = []
            i = 0
            while i < len(ex):
                v = ex[i]
                if v == op:
                    n1 = str(stack.pop())
                    n2 = str(ex[i+1])
                    stack.append(eval(n1 + v + n2))
                    i += 2
                else:
                    stack.append(v)
                    i += 1
            ex = stack
        answer = max(answer, abs(ex[0]))
    return answer

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))