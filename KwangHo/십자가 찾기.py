def sol(x,y,c):
  if x-c < 0 or x+c >= n or y-c < 0 or y+c >= m :
    
    return
  
  isC = False
  for i in pos:
    tx = x+i[0]*c
    ty = y+i[1]*c
    if not arr[tx][ty]=='*':
      isC = True
      break

  if not isC:
    dap.append([x+1,y+1,c])
    
    brr[x][y]='*'

    for i in pos:
      tx = x+i[0]*c
      ty = y+i[1]*c
      brr[tx][ty]='*'

    sol(x,y,c+1)


n,m=map(int,input().split())
arr=[]
brr=[]
pos=[[-1,0],[0,1],[1,0],[0,-1]]
dap=[]
for i in range(n):
  arr.append(list(input()))
  brr.append(list('.'*m))

for i in range(1,n-1):
  for j in range(1,m-1):
    if arr[i][j]=='*' : 
      
      sol(i,j,1)

if arr == brr:
  print(len(dap))
  for i in dap:
    print(i[0],i[1],i[2])
else :
  print(-1)

'''
또시간초과!!
리스트.apppend함수랑 set함수 사용하는순간
시간이 많이 걸리는가 보다!!

미리 만들어 놓고
마지막 비교하니 바로 통과댔다.
'''