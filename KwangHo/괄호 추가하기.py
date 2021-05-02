def sol(idx,s):
  global answer

  if idx == len(ops):
    answer = max(answer,int(s))
    return

  first = str(eval(s + ops[idx] + nums[idx + 1]))
  sol(idx + 1, first)

  if idx + 1 < len(ops):
    second = str(eval(nums[idx + 1] + ops[idx + 1] + nums[idx + 2]))
    second = str(eval(s + ops[idx] + second))
    sol(idx + 2, second)  


n=int(input())
arr=input()
answer = -999999
nums=[]
ops=[]

for i in arr:
  nums.append(i) if i.isdigit() else ops.append(i)

sol(0,nums[0])
print(answer)
'''
괄호를 합으로 도출하기가 쉽지 않아서!!
별도 테스트케이스에서 계쏙 막혔다.
답변보고 재코딩했다.
제출하지않고 며칠뒤에 다시 생으로 풀어봐야겟다.
'''