a,b,c,x,y=map(int,input().split())
z=0
s=a*x+b*y

while True:
  t = a*(max(0,x-1))+b*(max(0,y-1))+(z+2)*c
  if s > t:
    x-=1
    y-=1
    z+=2
    s=t
  else :
    break
print(s)
'''
이런 극한의 이득을 위해
안먹는 치킨을 더사야하는 경우라니

양념/후라이드로 값세팅후
반반 증가하면서 양념 후라이드 감소해서
최소값 찾기
'''