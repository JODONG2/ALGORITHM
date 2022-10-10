def recur(idx,num,visit):
    if idx == num : 
        return 1 
    if num in visit:
        return 0
    visit.append(num)
    return recur(idx,seq[num-1],visit)

n = int(input())

seq = [] 
for _ in range(n):
    seq.append(int(input())) 
ans = [] 
for idx,num in enumerate(seq): 
    if recur(idx+1,num,[]):
        ans.append(idx+1)
print(len(ans)) 
for a in ans:
    print(a)

# for s in seq:
#     print(s)