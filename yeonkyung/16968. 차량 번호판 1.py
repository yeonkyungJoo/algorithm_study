dic = {
    'c' : 'abcdefghijklmnopqrstuvwxyz',
    'd' : '0123456789'
}

s = input()
total = 1
for idx, ch in enumerate(s):
    if idx != 0 and s[idx-1] == ch:
        total *= len(dic[ch])-1
    else:
        total *= len(dic[ch])
print(total)