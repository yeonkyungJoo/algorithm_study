from math import inf

n,m=map(int,input().split())
arr=[[False]*(n+1) for i in range(n+1)]
cnt=[0]*(n+1)
dap=inf

for i in range(m):
  x,y=map(int,input().split())
  arr[x][y]=True
  arr[y][x]=True
  cnt[x]+=1
  cnt[y]+=1

for i in range(1,n-1):
  for j in range(i+1,n):
    if arr[i][j]:
      for k in range(j+1,n+1):
        if arr[i][k] and arr[j][k]:
          s = cnt[i]+cnt[j]+cnt[k]-6
          dap=min(dap,s)
          
if dap==inf : print(-1)
else : print(dap)
'''
3명의 친구일때 그 친구들의
친구들 값을 더한후!!
각 친구들마다 중복된값 -2 * 3명 하고
최소값을 구한다!
'''