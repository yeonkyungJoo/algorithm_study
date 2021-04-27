n=int(input())
arr=[False]*(n*50+1)
cnt=0
for i in range(n+1): #1
  for j in range(n+1-i): #5
    for k in range(n+1-i-j): #10
      s=i*1+j*5+k*10+(n-i-j-k)*50
      if not arr[s]:
        arr[s]=True
        cnt+=1
print(cnt)
'''
처음에 백트래킹으로 풀었는데 자꾸 시간초과 나서
최적화해도 나서 다른 방식으로 풀었다!?
혹시 백트래킹으로 푸신분 있나요?

arr=[1,5,10,50]
s = [False]*1005
n=0
cnt=0

def sol(su,cn):
  #global n
  global cnt
  if cn==n:
    if not s[su]:
      s[su] = True
      cnt+=1
    return
  
  #global arr
  for i in range(4):
    sol(su+arr[i],cn+1)

n = int(input())
sol(0,0)
print(cnt)
'''
