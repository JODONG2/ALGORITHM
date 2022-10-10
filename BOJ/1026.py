_ = input() 
a = sorted(map(int,input().split()), reverse = True) 
b = sorted(map(int,input().split())) 
answer = 0 
for A,B in zip(a,b): 
    answer += int(A) * int(B)
print(answer )