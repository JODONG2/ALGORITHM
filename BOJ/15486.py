import sys 
if __name__ =="__main__":
    N = int(input()) 
    schedules = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    print(schedules)
    money = [0 for _ in range(N+1)] 
    m = 0 
    for i,schedule in enumerate(schedules):
        t,pay = schedule[0], schedule[1] 
        m = max(money[i], m)
        if i+t <= N :
            money[i+t] = max(m+pay, money[i+t])
        # print(money)
    print(max(money))



