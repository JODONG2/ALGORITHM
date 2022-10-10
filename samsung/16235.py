"""
상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. S2D2는 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다. 
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 하나의 칸에 여러 개의 나무가 있다면, 
나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.

가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 N, M, K가 주어진다.

둘째 줄부터 N개의 줄에 A배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c]이다.
다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.

첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.
"""
answer = [] 
import sys
import heapq
def input_data():
    n,m,k = map(int,sys.stdin.readline().split())
    a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    forest_cnt= [[0 for _ in range(n)] for _ in range(n)] 
    forest_age = [[[] for _ in range(n)] for _ in range(n)]
    trees = set()
    for _ in range(m): 
        x,y,age = map(int,sys.stdin.readline().split()) 
        x-=1
        y-=1
        heapq.heappush(forest_age[x][y],age)
        forest_cnt[x][y] += 1 
        trees.add((x,y))
    # trees = deque(sorted([list(map(int,sys.stdin.readline().split())) for _ in range(m)],key= lambda x: x[2]))
    
    # an = int(input())
    # answer.append(an)
    return n,m,k,a,trees,forest_cnt,forest_age

#r과 c는 1부터 시작한다.
def sp (trees,base): 
    #TODO: 나무의 나이만큼 양분을 먹고 나이가 1 증가, 어린 나무부터 양분을 먹음,  양분이 부족해 자신의 나이만큼 양분 못먹으면 바로 죽음
    # 2 1 3
    # 3 2 3
    temp = []
    for i,tree in enumerate(trees): 
        if base[tree[0]][tree[1]] - tree[2] >= 0 : 
            base[tree[0]][tree[1]] -= tree[2] 
            tree[2] = tree[2]+1 
        else :
            temp.append(i)
    for i in temp[::-1]:
        x,y,age = trees[i]
        base[x][y] += age//2
        del trees[i]
# def su (trees): 
#     #TODO: 봄에 죽은 나무가 양분으로 변함, 해당칸에 양분 += 죽은나무//2 
#     # for tree in trees : 
#     #     if tree[2] < 0 : 
#     #         base[tree[0]][tree[1]] += (-tree[2])//2 
#     #         del tree
#     len_trees = len(trees)
#     print(trees)
#     for i in range(len_trees-1, -1, -1):
#         if trees[i][2] < 0 : 
#             del trees[i]
#     print(trees)
def fa (trees,n):
    #TODO: 나이가 5의 배수이면 번식함 인접한 8개의 칸에 1살인 나무가 생김
    dx = [-1,-1,-1, 0,0, 1,1,1]
    dy = [1,0,-1, 1,-1, 1,0,-1]
    make = deque()
    for tree in trees : 
        if tree[2] % 5 == 0 : 
            for px, py in zip(dx,dy): 
                nx,ny = tree[0]+px, tree[1]+py
                if 0<=nx<n and 0<=ny<n : 
                    make.append([nx,ny,1])
    for ma in make : 
        trees.appendleft(ma)

def wi (a,base,n): 
    #TODO: s2d2가 땅에 양분을 추가함. 추가되는 양분의 양은 A[r][c] 입력 
    for i in range(n):
        for j in range(n): 
            base[i][j] += a[i][j]

if __name__ == "__main__": 
    n,m,k,a,trees = input_data()
    base = [[5 for _ in range(n)] for _ in range(n)] 
    for _ in range(k): 
        sp(trees,base)
        # su(trees)
        fa(trees,n)
        wi(a,base,n)
    # print(len([tree for tree in trees if tree[2]!=-1]))
    print(trees)
    print(len(trees))

    # test_case = int(input()) 
    # ans = []
    # for _ in range(test_case):
    #     n,m,k,a,trees = input_data()
    #     base = [[5 for _ in range(n)] for _ in range(n)] 
    #     for _ in range(k): 
    #         sp(trees,base)
    #         su(trees,base)
    #         fa(trees,n)
    #         wi(a,base,n)
    #     ans.append(len(trees))
    # print(ans)
    # print(answer)
    # assert ans == answer 
"""
5
1 1 1
1
1 1 1
1
1 1 4
1
1 1 1
0
5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
2
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
15
5 2 3
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
13

"""