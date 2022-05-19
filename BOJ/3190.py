"""
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
"""
#TODO: 방향전환 
#TODO: 벽, 자기자신을 물면 죽음
#TODO: 사과먹으면 길이 + 1
import pdb
from collections import deque

def move(dir, answer, snake, time): 
    dir_y = [1,0,-1,0]
    dir_x = [0,1,0,-1]
    for _ in range(time):
        next_position = [snake[-1][0]+dir_x[dir], snake[-1][1]+dir_y[dir]]
        if next_position in snake : 
            return (True, answer)
        else: 
            snake.append([snake[-1][0]+dir_x[dir], snake[-1][1]+dir_y[dir]])

        if snake[-1] in apple_position : 
            del apple_position[apple_position.index(snake[-1])]
        elif snake[-1][0] >= N+1 or snake[-1][1] >=N+1 or snake[-1][0] <= 0 or snake[-1][1] <=0 :
            return (True, answer)
        else:
            snake.popleft()
        answer += 1
    return (False,answer)

def snake_game(dir_time:list,apple_position:list,N:int)-> int:
    if(dir_time[0][1] == "L"):
        return dir_time[0][0]
    snake = deque([[1,1]])
    dir = 0
    answer =1
    time_before = 0 
    while dir_time :
        #pdb.set_trace()
        time, turn = dir_time.popleft()
        time_sub = int(time)- time_before
        flag, answer = move(dir, answer, snake, time_sub)
        if flag:
            return answer 
        if turn == "D": dir +=1
        elif dir - 1 >= 0 :
            dir -=1
        elif dir - 1 <0 :
            dir = 3
        dir = dir % 4
        time_before = int(time)
    flag,answer = move(dir,answer,snake,N)
    if flag:
        return answer
            
    
if __name__ == "__main__":
    N = int(input())
    apple_cnt = int(input()) 
    apple_position = deque()
    for _ in range(apple_cnt):
        apple_position.append(list(map(int,input().split())))
    dir_change_cnt = int(input())
    dir_time = deque()
    for _ in range(dir_change_cnt):
        dir_time.append(list(input().split()))

    print(snake_game(dir_time, apple_position, N))
         
    
"""
5
0
5
4 D
8 D
12 D
15 D
20 L

8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D

8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
"""