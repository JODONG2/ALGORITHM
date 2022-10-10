def check():
    for i in range(n):
        for j in range(i+1,n):
            if abs(position[j] - position[i]) == abs(i-j) :
                return False 
    return True 
def f1(index):
    global ans 
    if check():
        ans+=1 
    for i in range(index+1,n):
        for j in range(i+1,n):
            position[i],position[j] = position[j],position[i]
            f1(i)
            position[i],position[j] = position[j], position[i]
n = int(input()) 
position = [i for i in range(n)] 
ans = 0 
f1(-1)
print(ans)