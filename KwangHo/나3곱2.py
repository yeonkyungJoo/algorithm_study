
n=int(input())
arr=list(map(int,input().split()))
brr=[]
che=[0]*len(arr)

arr.sort()
brr.append(arr[0])
che[0]=1

idx=0
while True:
  if brr[idx]*2 in arr and che[arr.index(brr[idx]*2)]==0:
    che[arr.index(brr[idx]*2)]=1
    brr.append(brr[idx]*2)
  elif brr[idx]%3==0 and brr[idx]//3 in arr and che[arr.index(brr[idx]//3)]==0:
    che[arr.index(brr[idx]//3)]=1
    brr.append(brr[idx]//3)
  else:
    break
  idx+=1
idx=0
while True:
  if brr[idx]*3 in arr and che[arr.index(brr[idx]*3)]==0:
    che[arr.index(brr[idx]*3)]=1
    brr.insert(0,brr[idx]*3)
  elif brr[idx]%2==0 and brr[idx]//2 in arr and che[arr.index(brr[idx]//2)]==0:
    che[arr.index(brr[idx]//2)]=1
    brr.insert(0,brr[idx]//2)
  else:
    break

for i in brr:
  print(i,end=' ')

'''
쉬운문제를 어렵게 생각해서 먼가 삥삥 돌았다.
자꾸 백트래킹으로 생각해서
그냥 앞쪽 경우의수 돌고
뒤쪽 경우의 수 돌면 끝인데 ㅠ!!
'''