"""
상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. S2D2는 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다. 
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 하나의 칸에 여러 개의 나무가 있다면, 
나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 N, M, K가 주어진다.

둘째 줄부터 N개의 줄에 A배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c]이다.
다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.

첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.
"""
from collections import deque
import sys
input = sys.stdin.readline

def spring():
    global answer 
    for i in range(n):
        for j in range(n):
            len_t = len(t[i][j])
            for k in range(len_t):
                if t[i][j][k] <= no[i][j]:
                    no[i][j] -= t[i][j][k]
                    t[i][j][k] += 1
                else:
                    for _ in range(k, len_t):
                        no[i][j] += t[i][j].pop() // 2
                        answer -= 1 
                    break
                
def fall():
    global answer
    for i in range(n):
        for j in range(n):
            for k in t[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            t[x][y].appendleft(1)
                            answer+=1
            no[i][j] += s[i][j]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
answer = m 
s = []
t = [[deque() for _ in range(n)] for _ in range(n)]
no = [[5] * n for _ in range(n)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    t[x - 1][y - 1].append(z)
for i in range(k):
    spring()
    fall()
print(answer)



    
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