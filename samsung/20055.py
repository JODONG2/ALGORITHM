"""
길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다. 
벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있으며, 각 칸에는 아래 그림과 같이 1부터 2N까지의 번호가 매겨져 있다.
벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동한다. 
i번 칸의 내구도는 Ai이다. 

1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"라고 한다.
컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 

로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다. 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다
컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.

벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.
"""
# from collections import deque 
# robot_key = 1 
# def f1 (belt1,belt2,robot,n):
#     belt2.appendleft(belt1.pop())
#     belt1.appendleft(belt2.pop())
#     if belt1[n-1][1] != 0 : 
#         del robot[belt1[n-1][1]]
#         belt1[n-1][1] = 0
#     key_list = list(robot.keys()) 
#     for key in key_list :
#         robot[key] +=1
#         if robot[key]+1 == n-1 and belt1[robot[key]+1][0] > 0 : 
#             belt1[robot[key]+1][0] -= 1 
#             belt1[robot[key]][1] = 0 
#             del robot[key] 
#         elif robot[key]+1 < n and belt1[robot[key]+1][1] == 0 and belt1[robot[key]+1][0] != 0 :
#             belt1[robot[key]][1] = 0 
#             belt1[robot[key]+1][1] = key 
#             belt1[robot[key]+1][0] -= 1 
#             robot[key] +=1 
        

# # def f2 (belt1,robot):
# #     key_list = list(robot.keys())
# #     # key_list.sort() 
# #     for key in key_list : 
# #         y = robot[key]
# #         if y+1 == n-1 and belt1[y+1][0] > 0 : 
# #             del robot[key] 
# #             belt1[y][1] = 0 
# #             belt1[y+1][0] -= 1
# #         elif y+1 < n and belt1[y+1][1] == 0 and belt1[y+1][0] != 0: 
# #             robot[key] = y+1 
# #             belt1[y][1] = 0 
# #             belt1[y+1][1] = key
# #             belt1[y+1][0] -= 1 

# def f3 (belt1,robot):
#     if belt1[0][0] != 0 : 
#         global robot_key 
#         belt1[0][0] -=1 
#         belt1[0][1] = robot_key 
#         robot[robot_key] = 0
#         robot_key += 1
        
    
# def f4 (belt1,belt2,k):
#     for b1,b2 in zip(belt1,belt2): 
#         if b1[0] <= 0 : 
#             k -= 1
#             if k == 0 : return False 
#         if b2[0] <= 0 :
#             k-= 1 
#             if k==0 : return False 
#     return True 

# if __name__ == "__main__":
#     n,k = map(int,input().split()) 
#     belt_temp = list(map(int,input().split())) 
#     belt = [[a,0] for a in belt_temp]
#     len_belt = len(belt)
#     belt1 = deque(belt[:len_belt//2])
#     belt2 = deque(belt[len_belt//2:])
#     answer = 0 
#     robot = {}
#     while True : 
#         f1(belt1,belt2,robot,n)
#         # f2(belt1, robot)
#         f3(belt1,robot)
#         if f4(belt1,belt2,k) :
#             answer +=1 
#         else:
#             answer+=1
#             break 
#     print(answer)

"""
3 2
1 2 1 2 1 2

3 6
10 10 10 10 10 10

4 5
10 1 10 6 3 4 8 2
"""
import sys 
input = sys.stdin.readline 
from collections import deque 
n, k = map(int, input().split()) 
belt = deque(list(map(int, input().split()))) 
robot = deque([0]*n) 
res = 0 
while 1: 
    belt.rotate(1) 
    robot.rotate(1) 
    robot[-1]=0 #로봇이 내려가는 부분이니 0 
    if sum(robot): #로봇이 존재하면 
        for i in range(n-2, -1, -1): #로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터 
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1: 
                robot[i+1] = 1 
                robot[i] = 0 
                belt[i+1] -= 1 
        robot[-1]=0 #이 부분도 로봇 out -> 0임 
    if robot[0] == 0 and belt[0]>=1: 
        robot[0] = 1 
        belt[0] -= 1 
    res += 1 
    if belt.count(0) >= k: 
        break 
print(res)

