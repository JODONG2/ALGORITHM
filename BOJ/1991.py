import sys 

def pre(now):
    ans=''
    for a in dict[now]:
        if a =='.':
            continue
        ans += a 
        ans += pre(a)
    return ans
def post(now):
    ans = ''
    for a in dict[now]:
        if a=='.':
            continue 
        ans+=post(a) 
    ans+=now 
    return ans 
def inorder(now):
    ans = ''
    if dict[now][0] != '.':
        ans += inorder(dict[now][0])
    ans += now 
    if dict[now][1] != '.':
        ans += inorder(dict[now][1])
    return ans 
    
cnt = int(sys.stdin.readline()) 
dict= {} 
for _ in range(cnt): 
    a,b,c = sys.stdin.readline().split()
    dict[a] = [b,c]
print('A'+pre('A'))
print(inorder('A'))
print(post('A'))