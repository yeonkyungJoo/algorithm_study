def Change(num,index): #진수구해서 리턴
    arr= '0123456789ABCDEF'
    a,b = divmod(num,index)
    if a==0:
        return arr[b]
    else:
        return Change(a,index)+arr[b]

def solution(n, t, m, p):
    answer = ''
    
    brr=''
    number=0
    while len(brr)<=t*m: # t*m까지의 길이만큼
        brr += Change(number,n)
        number+=1
    
    for i in range(p-1,t*m,m):
        answer+=brr[i]
        
    
    return answer