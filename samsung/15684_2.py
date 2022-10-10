"""
첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)xH)

둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.

가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.

가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가한다. 세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.

입력으로 주어지는 가로선이 서로 연속하는 경우는 없다.

5 5 6
1 1
3 2
2 3
5 1
5 4

"""
import sys
N,M,H = map(int,sys.stdin.readline().split())
lines = [list(map(int,sys.stdin.readline().split())) for _ in range(M)] 

def make_line():  #사다리 위치 
    ret = [[0 for _ in range(N+1)] for _ in range(H+1)] 
    for line in lines:
        ret[line[0]][line[1]] = 1 
    return ret 

line = make_line() 


def check():  #사다리 결과 
    for i in range(1,N): 
        position = i 
        for j in range(1,H+1): 
            if line[j][position] == 1 : 
                position +=1 
            elif line[j][position-1] == 1 :
                position -=1
        if position != i : 
            return False 
    return True 

result = 4 

def dfs(count:int, x:int, y:int , result ):
    if count >= result : return result 
    if check(): 
        result = count 
        return count
    if count == 3 : 
        return result 
    for i in range(x,N): 
        for h in range(y,H+1): 
            if line[h][i] ==0 and line[h][i-1] == 0 and line[h][i+1] == 0 : 
                line [h][i] = 1 
                result = dfs(count+1,x,y,result)
                line[h][i] = 0 
                if result ==0 :
                    return result 
    return result
if __name__ == "__main__":
    result = dfs(0,1,1,4)
    if result ==4 : 
        result = -1 
    print(result)

#TODO: dfs
    #TODO: 3개까지 추가설치가능 count>3 return 
    #TODO: 


