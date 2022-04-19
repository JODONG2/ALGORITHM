n,m = map(int,input().split()) 
position = list(map(int,input().split()))
left = sorted([i for i in position if i <0])
right = sorted([i for i in position if i>0], reverse = True)
answer = 0 

for i in range(0,len(left),m):
    answer +=  -(left[i] * 2)

for j in range(0,len(right),m) : 
    answer += (right[j] * 2)

if left and right : 
    if -left[0] > right[0] : 
        answer -= -left[0] 
    else : 
        answer -= right[0]
elif left : 
    answer += left[0] 
elif right : 
    answer -= right[0]
print(answer)
