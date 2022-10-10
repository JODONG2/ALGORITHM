"""
루빅스 큐브가 모두 풀린 상태에서 시작한다. 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색이다.

루빅스 큐브를 돌린 방법이 순서대로 주어진다. 이때, 모두 돌린 다음에 가장 윗 면의 색상을 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다. 각 테스트 케이스는 다음과 같이 구성되어져 있다.

첫째 줄에 큐브를 돌린 횟수 n이 주어진다. (1 ≤ n ≤ 1000)
둘째 줄에는 큐브를 돌린 방법이 주어진다. 각 방법은 공백으로 구분되어져 있으며, 
첫 번째 문자는 돌린 면이다. U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다. 
두 번째 문자는 돌린 방향이다. +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향이다.

각 테스트 케이스에 대해서 큐브를 모두 돌린 후의 윗 면의 색상을 출력한다. 
첫 번째 줄에는 뒷 면과 접하는 칸의 색을 출력하고, 두 번째, 세 번째 줄은 순서대로 출력하면 된다. 흰색은 w, 노란색은 y, 빨간색은 r, 오렌지색은 o, 초록색은 g, 파란색은 b.
"""
#TODO: u -> l,r,f,b 바뀜 
#TODO: d -> l,r,f,b 
#TODO: f -> u,d,l,r
# dic = {"U":[l,r,b,f], "D":[l,r,b,f], "L":[u,d,f,b], "R":[u,d,f,b], "F": [u,d,l,r] , "B": [u,d,l,r]}
def spin(comm:list, dic:dict):
    #comm[0] 바라보는면 
    #comm[1] 회전방향 - : 시계 + : 반시계 
    #dic = {"U":[l,r,b,f], "D":[l,r,b,f], "L":[u,d,f,b], "R":[u,d,f,b], "F": [u,d,l,r] , "B": [u,d,l,r]}
    if comm[0] == "U":
        l,r,b,f = dic[comm[0]]
        #0번째 
    elif comm[0] == "D": 
        l,r,b,f = dic[comm[0]] 
        #2번째줄
    elif comm[0] == "R": 
        u,d,f,b = dic[comm[0]] 
        #f -> [][2] d -> [][2] 

if __name__ == "__main__": 
    test_case = int(input()) 
    for t in range(1,test_case+1): 
        u = [['w' for _ in range(3)] for _ in range(3)] 
        d = [['y' for _ in range(3)] for _ in range(3)]
        b = [['o' for _ in range(3)] for _ in range(3)]
        f = [['r' for _ in range(3)] for _ in range(3)]
        r = [['b' for _ in range(3)] for _ in range(3)]
        l = [['g' for _ in range(3)] for _ in range(3)]
        dic = {"U":(l,r,b,f), "D":(l,r,b,f), "L":(u,d,f,b), "R":(u,d,f,b), "F": (u,d,l,r) , "B": (u,d,l,r)}
        q = [u,d,l,r,f,b]
        count = int(input()) 
        comm = list(input().split()) 
        #comm[0] 바라보는면 
        #comm[1] 회전방향 - : 시계 + : 반시계 
        print(comm)

"""
4
1
L-
2
F+ B+
4
U- D- L+ R+
10
L- U- L+ U- L- U- U- L+ U+ U+
"""
