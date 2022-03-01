import sys 

def input_data() : 
    N,M = map(int,sys.stdin.readline().split()) 
    shark = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    return N,M,shark

def cal_distance(N:int, M:int, arr:list)->int : 
    answer = 0 
    maxi = max(N,M)
    temp_arr = [[i,j] for i in range(N) for j in range(M) if not [i,j] in arr]
    for origin in temp_arr:
        distance = maxi
        for compare in arr: 
            x = abs(origin[0]-compare[0])
            y = abs(origin[1]- compare[1])
            x_y = min(x,y) + abs(x-y)
            distance = min(distance, x_y)
        answer = max(answer, distance)
    return answer
        
            
def safe_distance(N:int,M:int,shark:list)-> int:
    shark_position = []
    for x in range(N):
        for y in range(M): 
            if shark[x][y] == 1 :
                shark_position.append([x,y])
    return cal_distance(N,M,shark_position)

if __name__ == "__main__":
    N,M,shark = input_data() 
    print(safe_distance(N,M,shark))
"""
5 4           
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1

7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
"""