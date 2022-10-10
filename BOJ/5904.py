def recursion(moo,cnt,length,n):
    if length > n :
        return moo[n]
    tmp = 'm'+'o'*(cnt+2)
    return recursion(moo + tmp + moo,cnt+1, length*2 + cnt+3, n)

print(recursion('moo',0,3,int(input())))

"""
3 + 3 + 3 
0
moo  3
1
moo mooo moo 3 + 4 + 3 
2
moo mooo moo moooo moo mooo mooo 7 + 4 + 7
3 
moo mooo moo moooo moo mooo mooo 18 + 5 + 18
4
36 + 6 + 36 
"""