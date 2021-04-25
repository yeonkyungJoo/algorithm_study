n=input()
d= 26 if n[0]=='c' else 10
for i in range(1,len(n)) :
  if n[i-1]==n[i]:
    if n[i]=='c':
      d*=25
    else:
      d*=9
  else :
    if n[i]=='c':
      d*=26
    else:
      d*=10
print(d)
'''
전값과 비교하여 같으면 -1한 값을 곱해주고
아니면 그냥 곱해주는 식으로!!
'''