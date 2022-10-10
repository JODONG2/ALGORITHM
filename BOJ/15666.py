"""
4 4
1 1 2 2

4 2
9 7 9 1

1 1
1 7
1 9
7 7
7 9
9 9
"""

import sys 
# def dfs(index,limit,arr):
#     if limit == 0 : 
#         print(*arr)
#         return 
#     for i in range(index,n):
#         if not arr : 
#             arr.append(seq[i])
#             dfs(i,limit-1,arr) 
#             arr.pop()
#         elif seq[i] != arr[-1] : 
#             arr.append(seq[i])
#             dfs(i,limit-1,arr)
#             arr.pop()
#         elif i==index : 
#             arr.append(seq[i])
#             dfs(i,limit-1,arr)
#             arr.pop()
def dfs(limit,arr):
    if limit == 0 : 
        print(*arr)
        return 
    for i in range(n):
        if seq[i] in arr: 
            continue
        arr.append(seq[i])
        dfs(limit-1,arr)
        arr.pop()
n,m = map(int,sys.stdin.readline().split()) 
# seq = list(set(list(map(int,sys.stdin.readline().split()))))
seq = list(map(int,sys.stdin.readline().split()))
seq.sort()
dfs(m,[])