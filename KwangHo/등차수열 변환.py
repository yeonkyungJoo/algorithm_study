n=int(input())
arr=list(map(int,input().split()))
dap=-1

if n==1 or n==2:
  print(0)
else :
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      #print(i,j)
      a1=arr[0]+i
      a2=arr[1]+j
      d=a2-a1
      cnt=0
      if i!=0: cnt+=1
      if j!=0: cnt+=1
      isC = False

      for k in range(2,len(arr)):
        a2+=d
        if arr[k] == a2 : continue

        if arr[k]+1==a2 or arr[k]-1==a2:
          cnt+=1
        else :
          isC = True
          break
      
      if not isC:
        #if dap==-1 : dap=9999999
        #dap=min(dap,cnt)
        if dap==-1 or cnt < dap:
          dap=cnt
  print(dap)
'''
그냥 백트래킹으로 푸니깐 시간초과나서
가지치기하면서 컷팅해도 안돼길래!!
아예 다른방식으로 풀었다.!!
'''