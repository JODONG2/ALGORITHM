def deliver(last,sd,trg, c) : 
    change = False 
    ld = last
    for i in range(ld,-1,-1):
            if trg[i] == 0 : 
                continue
            if change : 
                last = i
                change = False 
            if c > 0 and trg[i] - c <= 0 : 
                sd -= trg[i]
                c = c - trg[i]
                trg[i] = 0  
                change = True 
            elif c > 0 and trg[i] - c > 0  :
                trg[i] -= c 
                sd -= c 
                last = i
                change = False 
                break 
            if c == 0 and not change: 
                break 
    return last , sd 


def solution(cap, n, deliveries, pickups):
    answer = -1
    sd, sp = sum(deliveries), sum(pickups)
    ld = -1 
    lp = -1
    for i in range(n-1,-1,-1):
        if ld != -1 and lp != -1 : 
            break 
        if ld == -1 and deliveries[i] != 0 : 
            ld = i 
        if lp == -1 and pickups[i] != 0: 
            lp = i 
    
    ans = 0 
    
    while not(sd == 0 and sp == 0) :
        ans += (max(ld,lp)+1) * 2 
        ld,sd = deliver(ld,sd,deliveries,cap)
        lp,sp = deliver(lp, sp, pickups,cap)
        if sp == 0 : lp = -1 
        if sd == 0 : ld = -1
        
    return ans


print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
