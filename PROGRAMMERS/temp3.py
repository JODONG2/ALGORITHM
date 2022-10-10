from collections import deque

def ShiftRow(rc):
    rc.appendleft(rc.pop())

def Rotate(rc,R,C):
    ru = rc[0][C-1]
    ld = rc[R-1][0]
    rc[0].rotate(1)
    rc[R-1].rotate(-1)
    for i in range(R,2,-1):
        rc[R-i][0] = rc[R-i+1][0]
        rc[i-1][C-1] = rc[i-2][C-1]
    rc[1][C-1] = ru 
    rc[R-2][0] = ld
    
def solution(rc, operations):
    answer = [[]]
    R = len(rc)
    C = len(rc[0])
    for i in range(R):
        rc[i] = deque(rc[i])
    rc = deque(rc)
    for operation in operations:
        if operation == "Rotate":
            Rotate(rc,R,C)
        else:
            ShiftRow(rc)
    answer = [list(rc[i]) for i in range(R)]
    return answer
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate", "ShiftRow"]))