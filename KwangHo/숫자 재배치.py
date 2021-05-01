from itertools import permutations

a,b = input().split()
b=int(b)
arr = list(map(''.join,permutations(a)))
c=-1

for i in arr:
  t = int(i)
  if t < b and i[0]!='0':
    c=max(c,t)
print(c)  
'''
아~오
시간초과 걸릴까봐 가지치기 햇는데
자꾸 틀리다고 해서
그냥 모든 경우의수 하니깐 됫다!!
'''