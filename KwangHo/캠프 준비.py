from itertools import combinations

n,l,r,x=map(int,input().split())
arr=list(map(int,input().split()))
brr=[]
cnt=0

for i in range(2,n+1):
  brr+=list(combinations(arr,i))

for i in brr:
  i=sorted(list(i))
  su = sum(i)
  st = i[0]
  en = i[len(i)-1]
  if su >= l and su <= r and en-st >= x :
    cnt+=1

print(cnt)
'''
중복없는 조합 구하고 , 정렬후
3가지 조건 충족할때마다 카운트!!
'''