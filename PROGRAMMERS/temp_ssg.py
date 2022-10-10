from itertools import accumulate 
from collections import deque 
def solution(v,q):
    print(q)
    print(v)

    answer = []
    len_v = len(v)
    origin_v = v[:]
    v = list(accumulate(v)) 
    temp_sum = [0 for _ in range(len_v+1)]
    mini = len_v 
    seq = deque()
    for a,b,c in q : 
        if a==1:
            alpha = 0 
            for i in range(len(seq)-1,-1,-1):
                if seq[i][0] > c : 
                    continue 
                else:
                    alpha = seq[i][1] 
                    break 
            if b-1 == -1 :
                answer.append(v[c]+alpha)
            else:
                answer.append(v[c]-v[b-1]+alpha)
        else: 
            temp = c - origin_v[b]
            origin_v[b] = c 
            temp_sum[b] += temp 
            mini = min(mini,b)
            if not seq:
                seq.append([b,temp])
            else:
                len_seq = len(seq)
                succ = False 
                for i in range(len_seq-1,-1,-1):
                    if seq[i][0] >  b : 
                        seq[i][1] += temp 
                    elif seq[i][0] == b :
                        seq[i][1] += temp 
                        succ = True 
                        break 
                    else : 
                        seq.insert(i+1,[b,seq[i][1]+temp])
                        succ = True 
                        break 
                if not succ : 
                    seq.appendleft([b,temp])
            print(seq)
    return answer 
# print(solution([1, 2, 3, 4, 5],[[1, 2, 4], [2, 3, 8], [1, 2, 4],[2,4,20],[1,0,4]]))
print(solution([1, 2, 3, 4, 5],[[2,4,2],[1, 2, 4], [2, 3, 8], [1, 2, 4],[2,4,20],[2,1,30],[1,2,4],[2,0,10]]))


