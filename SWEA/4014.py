
def search_path():
    n,x = map(int,input().split()) 
    world = [list(map(int,input().split())) for _ in range(n)]
    answer = 0 
    r_answer = 0 
    d_answer =0 
    for i in range(n): #가로 확인할거임 
        j = 0 
        succ_right = True 
        succ_down = True 
        while (succ_right or succ_down) and j < n: 
            if j == 0 :
                num_right = world[i][j] 
                cnt_right = 0 
                cnt_right2 = 1 
                num_down = world[j][i] 
                cnt_down = 0
                cnt_down2 = 1 
            else : 
                #오른쪽
                if succ_right :
                    if num_right == world[i][j]: 
                        if cnt_right == 0 : 
                            cnt_right2 += 1
                        else : 
                            cnt_right +=1
                            if cnt_right == x : 
                                cnt_right = 0 
                    elif num_right - world[i][j] == -1 :  #오르막길
                        if cnt_right2 >= x and cnt_right == 0: 
                            cnt_right2 = 1 
                            num_right = world[i][j]
                        else : 
                            succ_right = False 
                    elif num_right - world[i][j] == 1 : #내리막길 
                        if cnt_right != 0 : 
                            succ_right = False 
                        else : 
                            cnt_right +=1 
                            cnt_right2 = 0 
                            num_right = world[i][j]

                    else : 
                        succ_right = False 

                if succ_down : 

                    if num_down == world[j][i] :
                        if cnt_down == 0 : 
                            cnt_down2 +=1 
                        else : 
                            cnt_down +=1 
                            if cnt_down == x:
                                cnt_down = 0 
                    
                    elif num_down - world[j][i] == - 1 : 
                        if cnt_down2 >= x and cnt_down == 0 :
                            cnt_down2 = 1 
                            num_down = world[j][i] 
                        else : 
                            succ_down = False 
                    elif num_down - world[j][i] == 1 : 
                        if cnt_down != 0 :
                            succ_down = False 
                        else : 
                            cnt_down +=1 
                            cnt_down2 = 0
                            num_down = world[j][i]
                    else:
                        succ_down = False 
            j+=1
            
            if j == n : 
                if succ_down and cnt_down != 0 : 
                    succ_down = False 
                if succ_right and cnt_right != 0 :
                    succ_right = False 
        if succ_down : 
            d_answer+=1 
        if succ_right :
            r_answer +=1
    return r_answer +d_answer

if __name__ == "__main__":
    test_case = int(input())
    for t in range(1,test_case+1):
        answer = 0 
        answer = search_path()
        print(f"#{t} {answer}")
"""
1
6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2

1
7 2
1 1 1 1 2 1 1 
1 1 1 2 2 2 1 
2 2 2 2 2 2 2 
2 2 2 2 2 2 2 
2 2 2 2 2 2 2 
2 2 2 2 2 2 2 
2 2 2 2 2 2 2 

right -> 6 

"""