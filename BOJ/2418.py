import sys 
from collections import deque 
def data_input():
    H,W,L = map(int,sys.stdin.readline().split())
    word_map = [list(sys.stdin.readline()[:-1]) for _ in range(H)] 
    word = list(sys.stdin.readline()[:-1])
    return H,W,L,word_map,word

def find_word(H,W,L,word_map,word,wdic) : 
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dx = [0,0,-1,1] 
    dy = [1,-1,0,0]
    for h in range(H) : 
        for w in range(W):
            if wdic.get(word_map[h][w]):
                q = deque((h,w))
                while q :
                    h,w = q.popleft()
                    for ph,pw in zip(dx,dy):
                        nh,nw = h+ph, w+pw 
                        if 0<=nh<H and 0<=nw<W:
                            wdic[word_map[h][w]]


if __name__=="__main__":
    H,W,L,word_map,word = data_input()
    wdic = {}
    for i in range(L-1) : 
        if wdic.get(word[i]) : 
            wdic[word[i]].append(word[i+1])
        else : 
            wdic[word[i]] = [word[i+1]]
    # for i in range(L): 
    #     if i == 0 : 
    #         wdic[word[i]]= [word[i+1]]
    #         continue 
    #     if wdic.get(word[i]) : 
    #         wdic[word[i]].append(word[i-1])
    #         wdic[word[i]].append(word[i+1])
    #     else : 
    #         wdic[word[i]] = [word[i-1]]
    #         if not i == L-1 : 
    #             wdic[word[i]].append(word[i+1])
    print(wdic)
         
    # for word_m in word_map :
    #     print(word_m)
    # print(word)
    
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
            
