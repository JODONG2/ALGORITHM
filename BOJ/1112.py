

def f1(num,d,cnt):
    if cnt % 2 == 0:
        if (num) // abs(d) == 0:
            return str(abs(num))
        else: 
            return f1((num//abs(d)),d,cnt+1) +  str(num%abs(d))
    else :
        if num // d == 0 : 
            return str(abs(num))
        else:
            return f1(abs(num//d),d,cnt+1) + str(abs(num%d))

def f2(num,d):
    if num // d <= d : 
        return str(num)
    else:
        return f2(num//d, d) + str(num%d)

import sys 
x,b = map(int,sys.stdin.readline().split())
if b < 0 :
    print(f1(x,b,0))
else : 
    print(f2(x,b))