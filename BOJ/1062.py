import sys 

def bitmask(temp, depth, index):
    global ans 
    # print(depth,m)
    if depth == m : 
        cnt = 0 
        for c in cmd : 
            if c & temp == c : 
                cnt +=1
        ans = max(ans,cnt)
        return 
    for i in range(index+1, len_needs) : 
        bitmask(temp|(1<<dict[needs[i]]), depth+1, i)
ans = 0 
dict = {} 
alpha = 'antci' 
alpha_cnt = 1
for a in alpha: 
    dict[a] = alpha_cnt 
    alpha_cnt += 1 
n,m = map(int,sys.stdin.readline().split()) 
bit = 1 
bit = bit | 1 << dict['a']
bit = bit | 1 << dict['n'] 
bit = bit | 1 << dict['t']
bit = bit | 1 << dict['c'] 
bit = bit | 1 << dict['i'] 

cmd2 = [sys.stdin.readline()[4:-5] for _ in range(n)]
cmd = [] 
needs = []
bonus = 0 
for c in cmd2 : 
    temp = 1 
    if not c : 
        bonus+=1 
        continue
    for cm in c : 
        if not dict.get(cm) : 
            dict[cm] = alpha_cnt 
            alpha_cnt +=1 
            needs.append(cm)
            temp |= 1 << dict[cm]
    if temp == 1 : 
        bonus+=1
        continue 
    cmd.append(temp)
# print(bonus)
len_needs = len(needs)
# print(needs)
# print(cmd)
# print(bonus, needs, cmd, len_needs)
if m >= 5 and needs:
    bitmask(bit,5,-1) 
print(ans+bonus)

"""
26 25 
antaqtica
antawtica
antaetica
antartica
antattica
antaytica
antautica
antaitica
antaotica
antaptica
antaatica
antastica
antadtica
antaftica
antagtica
antahtica
antajtica
antaktica
antaltica
antaztica
antaxtica
antactica
antavtica
antabtica
antantica
antamtica
"""
# from itertools import combinations
# n, k = map(int, input().split())
# if k < 5:
#     print(0)
# else:
#     k -= 5
#     nece_chars = {'a', 'n', 't', 'i', 'c'}
#     input_chars = []
#     alpha = {ky: v for v, ky in enumerate(
#         (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
#     cnt = 0
#     for _ in range(n):
#         tmp = 0
#         for c in set(input())-nece_chars:
#             tmp |= (1 << alpha[c])
#         input_chars.append(tmp)
#     power_by_2 = (2**i for i in range(21))
#     for comb in combinations(power_by_2, k):
#         test = sum(comb)

#         ct = 0
#         for cb in input_chars:
#             if test & cb == cb:
#                 ct += 1

#         cnt = max(cnt, ct)
#     print(cnt)