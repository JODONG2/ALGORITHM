ans1 = 0  
ans2 = 0 
def cal(disc,len_emot, emoticons,users):
    ret1 = 0 
    info = [0 for _ in range(len(users))]
    for u,user in enumerate(users) : 
        for i in range(len_emot):
            if disc[i] >= user[0] : 
                info[u]+= emoticons[i] * ((100-disc[i])/100)
                if info[u] >= user[1] : 
                    info[u] = 0 
                    ret1 += 1
                    break
    return ret1, sum(info)
def f(disc,len_emot,per,emoticons,now,users): 
    global ans1
    global ans2
    if now == len_emot : 
        reg,money = cal(disc,len_emot, emoticons,users)
        if ans1<reg : 
            ans1 = reg 
            ans2 = money 
        elif ans1==reg and ans2<money : 
            ans2 = money
        return 
    for p in (per): 
        disc[now] = p 
        f(disc,len_emot,per,emoticons,now+1,users) 
def solution(users, emoticons):
    
    answer = []
    len_emot = len(emoticons)
    disc = [0 for _ in range(len_emot)]
    visit = [False for _ in range(len_emot)] 
    per = [10,20,30,40]
    #def f(disc,len_emot,per,emoticons,now,users): 
    f(disc,len_emot,per,emoticons,0,users)
    
    return [ans1,int(ans2)]
