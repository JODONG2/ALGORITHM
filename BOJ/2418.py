# 2418 단어 격자
def dp (target,arr,i,j,step, LE):
    if arr[i][j] in target:
        target.index


h,w,LE = map(int,input().split())
arr = []
table = [[0,0 for _ in range(w)] for _ in range(h)]
seq1 = [-1,0,1]
seq2 = [-1,0,1]
for _ in range(h):
    arr.append(list(input()))
target = list(input())
for i in range(h):
    for j in range(w):
        if (arr[i][j] in target) and table[i][j][1] == 0 :
            