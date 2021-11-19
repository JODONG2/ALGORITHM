#과제는 끝나지 않아
from collections import deque
t = int(input())
answer = 0
score = deque()
time = deque()
for _ in range(t):
    hw = list(map(int,input().split()))
    if hw[-1] == 1:
        answer += hw[1]
    elif not hw[0] == 0 : 
        hw[2] -= 1 
        time.append(hw[2])
        score.append(hw[1])
    elif hw[0] == 0:
        time[-1] -= 1
        if time [-1] == 0 :
            answer += score.pop()
print(answer)