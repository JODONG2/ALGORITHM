from copy import deepcopy 

answer = 0
cnt_6 = 0 
def input_data():
    n,m = map(int,input().split()) 
    room = []
    cctv = [] 
    global cnt_6
    for j in range(n):
        room.append(list(map(int,input().split())))
        for i in range(1,6):
            if i in room[-1] : 
                cctv.append([j,room[-1].index(i),i,True])
        cnt_6 += room[-1].count(6)
    # print(cnt_6,"+"*20)
    return n,m,room,cctv 

def show_r(room,n,m,x,y,cctv_show):
    while  y < m and room[x][y] != 6:
        cctv_show.add((x,y))
        y+=1 
    return cctv_show

def show_l(room,n,m,x,y,cctv_show):
    while y >= 0 and room[x][y] != 6:
        cctv_show.add((x,y))
        y-=1 
    return cctv_show

def show_u(room,n,m,x,y,cctv_show):
    while x >= 0 and room [x][y] != 6 : 
        cctv_show.add((x,y)) 
        x-=1 
    return cctv_show 

def show_d(room,n,m,x,y,cctv_show):
    while x < n and room [x][y] != 6 : 
        cctv_show.add((x,y)) 
        x+=1 
    return cctv_show 

#TODO: 1번 한 방향 
#TODO: 2번 180도 방향
#TODO: 3 = 90 degree 
#TODO: 4 = 3 direction
#TODO: 5 = all direction 
#TODO: CCTV = [x,y,type,is_used]
def show (room,n,m,cctv2,cctv_show2,cnt):
    
    if cnt == len(cctv2):
        global answer 
        answer = max(answer, len(cctv_show2)+cnt_6)
        # if len(cctv_show2)+cnt >= 20:
        #     print(cctv_show2, len(cctv_show2),answer ,n,m)
        #     for i in range(n):
        #         for j in range(m): 
        #             if (i,j) in cctv_show2 : 
        #                 print("S ",end="")
        #             else: 
        #                 print("N ",end="")
        #         print()

    cctv_show = deepcopy(cctv_show2)
    cctv = deepcopy(cctv2)
    for i,(x,y,type,used) in enumerate(cctv):
        if not used :
            continue 
        cctv[i][-1] = False

        if type == 1 :

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)
            # show(room,n,m,cctv,show_r(room,n,m,x,y,cctv_show),cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)
            # show(room,n,m,cctv,show_l(room,n,m,x,y,cctv_show),cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)

        elif type == 2 :
            cctv_show = deepcopy(cctv_show2)

            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)

        elif type == 3 : 
            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)
            
            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
        elif type == 4 : 
            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)

            show(room,n,m,cctv,cctv_show,cnt+1)
            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)

            cctv_show = deepcopy(cctv_show2)

        elif type == 5 : 
            cctv_show = deepcopy(cctv_show2)
            cctv_show = show_u(room,n,m,x,y,cctv_show)
            cctv_show = show_d(room,n,m,x,y,cctv_show)
            cctv_show = show_r(room,n,m,x,y,cctv_show)
            cctv_show = show_l(room,n,m,x,y,cctv_show)
            show(room,n,m,cctv,cctv_show,cnt+1)
            cctv_show = deepcopy(cctv_show2)

    answer = max(answer, len(cctv_show))
    

if __name__ == "__main__":
    n,m,room,cctv = input_data()
    show(room,n,m,cctv,set(),0)
    print(n*m - answer)

