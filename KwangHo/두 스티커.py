h,w=map(int,input().split())
n=int(input())
arr=[]
d=0

for i in range(n):
  trr=list(map(int,input().split()))
  arr.append(trr)

if h > w :
  h,w=w,h

for i in range(len(arr)-1):
  for j in range(i+1,len(arr)):
    for k1 in range(2):
      for k2 in range(2):
        if (arr[i][k1]+arr[j][k2] <= h and max([arr[i][1-k1],arr[j][1-k2]]) <= w) or (arr[i][k1]+arr[j][k2] <= w and max([arr[i][1-k1],arr[j][1-k2]]) <= h):
          s = arr[i][0]*arr[i][1]+arr[j][0]*arr[j][1]
          d = max([d,s])
print(d)
'''
2개합과 나머지2개중 맥스를 판안에 포함되는지
처음에 모든경우의수 체크 안할려고
가지치기 엄청했는데 먼가 잘못된는지 7%에서 계속 멈췃다.
그래서 전체경우의수 하니깐 통과;;;
(먼가 놓친 가지치기 있는듯햇다)
'''