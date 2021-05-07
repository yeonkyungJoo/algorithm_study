n=int(input())
Cranes = list(map(int,input().split()))
m=int(input())
Boxs = list(map(int,input().split()))
Cranes.sort()
Boxs.sort()
cnt=0

if Cranes[len(Cranes)-1] < Boxs[len(Boxs)-1]: #옮길수 없는 경우의 수 체크
  Boxs=[]
  cnt=-1

while len(Boxs)!=0:
  craneLen = len(Cranes)-1
  boxLen = len(Boxs)-1
  for i in range(boxLen,-1,-1):
    if Boxs[i] <= Cranes[craneLen]: #크레인 돌면서 작은값 있으며
      Boxs.pop(i)
      craneLen-=1
      if craneLen < 0 :
        break
  cnt+=1
print(cnt)

'''
> 크레인보다 박스값이 작으면 박스를 팝!!
박스를 다 소직할때까지 크레인을 순차적으로 돌린다.
크레인 다돌리면 카운트+1
그래서 박스 다 소진하면 끝!!
'''