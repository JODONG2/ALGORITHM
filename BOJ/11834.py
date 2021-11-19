#홀짝
num = int(input())
l = 0 
r = num 
while (l+1 < r) : 
    m = (l+r) // 2
    if m*(m+1) //2 < num : 
        l = m 
    else :
        r = m 
print(2 * num - r)