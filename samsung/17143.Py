

"""
칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.
낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다. 
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

낚시왕이 오른쪽으로 한 칸 이동한다.
낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
상어가 이동한다.

상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다. 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 
상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. 
d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

낚시왕이 잡은 상어 크기의 합을 출력한다.
"""
#TODO: 상어 위치 = x,y (x+s)//(R-1) %2 == 0 : 방향 같음 else : 방향 다름 
#TODO: [1,2,3,...,r,r-1,...,2] 반복 
r,c,m = map(int,input().split()) 
sharks = [list(map(int,input().split())) for _ in range(m)]

shark_dict = {} 
world = [[0 for _ in range(c)] for _ in range(r)]
for i,shark in enumerate(sharks):
    shark[0] -=1 
    shark[1] -=1 
    shark_dict[100+i+1] = shark
    world[shark[0]][shark[1]] = 100+i+1

r_position_d = [i for i in range(r)] + [j for j in range(r-2,0,-1)]
r_position_u = [i for i in range(r-1, -1, -1 )] + [j for j in range(1,r-1)]
c_position_r = [i for i in range(c)] + [j for j in range(c-2,0,-1)]
c_position_l = [i for i in range(c-1,-1,-1)] + [j for j in range(1,c-1)]
position = [0,r_position_u, r_position_d , c_position_r, c_position_l] 

answer = 0 
for pos in range(c): 
    catch = False 
    # for w in world : 
    #     print(w)
    # print("*"*50)
    for i in range(r):
        if not catch and world[i][pos] !=0 :
            answer += shark_dict[world[i][pos]][4]  
            del shark_dict[world[i][pos]]
            world[i][pos] = 0 
            catch = True 
        for j in range(c): 
            world[i][j] = 0
    if not shark_dict.keys():
        break 
    key_list = list(shark_dict.keys())
    for key in key_list: 
        x,y,s,d,z = shark_dict[key] 
        nx,ny = x,y
        if s != 0 :
            if d == 1 : 
                nx = position[d][((r-1)-x+s) % (r+(r-2))] 
                if ((r-1 - x + s) // (r-1)) % 2 : 
                    d = 2 
            elif d == 2 : 
                nx = position[d][(x+s)%(r+(r-2))]
                if ((x+s)//(r-1))%2 :
                    d= 1

            elif d==3 : 
                ny = position[d][(y+s)%(c+(c-2))]
                if ((y+s)//(c-1))%2 : 
                    d=4 
            elif d == 4 : 
                ny = position[d][(c-1-y + s) %(c+(c-2))]
                if ((c-1 - y + s ) // (c-1)) %2 : 
                    d= 3 

        if world[nx][ny] != 0 : 
            if shark_dict[world[nx][ny]][4] > z : 
                del shark_dict[key]
                continue
            else : 
                del shark_dict[world[nx][ny]] 
                world[nx][ny] = key 
        else : 
            world[nx][ny] = key 
        shark_dict[key] = [nx,ny,s,d,z]
# for w in world: 
#     print(w)
print(answer)
"""
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5

22


3 3 9
1 1 1000 1 1
1 2 999 2 2
2 1 1000 3 3
2 2 999 4 4
1 3 1000 1 5
3 1 999 2 6
2 3 1000 3 7
3 2 999 4 8
3 3 1000 1 9

50 50 19
4 9 21 1 999
50 50 4 4 500
50 49 222 3 200
50 48 12 2 45
50 47 36 1 900
2 3 20 3 444
4 8 4 2 49
3 3 40 4 51
2 2 460 2 4444
48 23 500 3 12
1 1 200 1 123
44 44 123 3 125
44 40 222 3 17
40 44 333 3 57
18 40 1 1 4
3 10 50 2 406
1 36 177 4 50
1 46 120 4 7
1 50 28 4 54

4 4 4 
1 1 1 1 1 
4 4 1 3 1 
1 4 1 3 1
4 1 1 2 1

1 위 2 아래 3 오른 4 왼 
4 15 4 
1 1 1 4 1 
4 15 1 2 1 
1 15 1 1 1
4 1 1 2 1

4 15 4 
1 5 1 3 1 
4 15 1 2 1 
1 15 1 1 1
4 5 1 3 1



4 15 4 
1 5 1 3 1 
4 15 1 3 1 
1 15 1 3 1
4 5 1 3 1


4 4 4 
1 1 1 1 1 
4 4 1 3 1 
1 4 1 3 1
4 1 1 2 1

https://www.acmicpc.net/board/view/36179
"""