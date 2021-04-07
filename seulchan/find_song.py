'''
time: HH:MM -> 00:00 ~ 23:59
score <= 1439, C C# D D# E F F# G G# A A# B
infos: ["start,end,title,score", ...]

input: m, infos
output: title or "(None)"

- how to find exact "m" is contains the score
- if multiple sort with -> (end - start)
- if same -> remaining order

## solution
# create whole note from time
# find all match info
# sort it with time

start, end, title, score = info.split(',')
r = []

# count min
# time:  -> t
HH1, HH2 = start[:1], end[:1]
if HH2 == HH1 then t = MM2 - MM1
if HH2 > HH1 then
    # 12:00,13:06 -> (6-0) + (13-12)*60 = 66
    if MM1 < MM2: then (MM2 - MM1) + (HH2-HH1)*60
    # 12:05,15:01 -> (01-05+60) + (HH2-HH1-1)*60 -> (15-12)*60 + (01-05) = 180-4 = 176
    # else: MM1 - MM2 then (MM2-MM1+60) + (HH2-HH1-1)*60 = (MM2-MM1) + (HH2-HH1)
# create note
# CDEFGAB -> s = 7
s = len(score)
count, rest = divmod(t, s)
if not rest: note = count*score
else: note = f{count * score}{score[:rest-1]}

# check if matched
if m in r:  # O(n)
# added to r -> [(time, score, title)]
r.append((time, score, title))

# sort it with time and return title
if len(r) == 0: return '(None)'
r.sort(key=lambda x: x[0])
return sorted(r, key=lambda x: x[0])[0][2]
'''
from collections import Counter
def solution(m, musicinfos):
    def replace_hashtag(s):
        hastag = [
            ('C#', 'J'),
            ('D#', 'K'),
            ('F#', 'I'),
            ('G#', 'L'),
            ('A#', 'H'),
        ]
        for h in hastag:
            s = s.replace(h[0], h[1])
       	return s 
    
    r = []
    m = replace_hashtag(m)
    for info in musicinfos:
        start, end, title, score = info.split(',')
        score = replace_hashtag(score)
        HH1, HH2 = int(start[:2]), int(end[:2])
        MM1, MM2 = int(start[3:]), int(end[3:])
        t = (MM2 - MM1) + (HH2-HH1)*60

        s = len(score)
        real_score = score[:t]
        if s >= t:
            if m in real_score:
                r.append((t, score, title))
            continue
            
        count, rest = divmod(t, s)
        added = '' if not rest else score[:rest]
        note = f'{count * score}{added}'
        if m in note:
            r.append((t, score, title))
       
    if len(r) == 0:
        return '(None)'
    if len(r) == 1:
        return r[0][2]
    
    return sorted(r, key=lambda x: x[0])[0][2]

