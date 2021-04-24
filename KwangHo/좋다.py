n=int(input())
arr=list(map(int,input().split()))
arr.sort()

cnt = 0
for i in range(n):
  brr = arr[:i] + arr[i+1:]
  left = 0
  right = len(brr)-1
  while left<right:
    s = brr[left]+brr[right]
    if s == arr[i]:
      cnt+=1
      break
    if s < arr[i] : left+=1
    else : right-=1
print(cnt)

'''
처음에 조합으로 푸는줄 알고 고생하다가
(메모리초과/0예외처리때문에)근데도 틀림
분류에 이분탐색있어서 그렇게 푸니깐 바로됨!
- 그냥 전체 도는걸 이분탐색으로 가지치기 하면되는거였음
'''