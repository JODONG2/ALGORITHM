import sys 
cnt = int(input()) 
seq = list(map(int,sys.stdin.readline().split()))
set_seq = set(seq)

answer = 0 
zero_check = seq.count(0)>=3 

for i in range(cnt):
    num = seq[i] 
    for j in range(cnt):
        if i==j :
            continue 
        if num-seq[j] in set_seq:
            if num - seq[j] == seq[j] and seq.count(seq[j]) < 2 : 
                continue 
            if num - seq[j] == num and seq.count(num) <2 : 
                continue 
            if num == 0 and seq[j] == 0  and not zero_check: 
                continue
            answer+=1
            # print(num,seq[j])
            break 
print(answer)