import sys 
from collections import deque 
commands = int(sys.stdin.readline())
answer = deque()
temp = deque()
def recursive_undo(temp,answer,i): 
    while temp[-1-i]: 
        c,t = temp[-1-i].pop()
        if c == 'undo': 
            recursive_undo(temp,answer,i+1)
        answer.append((c,t))
answer = [] 
for _ in range(commands):
    command = input().split()
    if command[0] == 'type' :
        answer.append((command[1],command[2])) 
    elif command[0] == 'undo':
        temp2 = [] 
        while answer and int(answer[-1][1]) >= int(command[2]) - int(command[1]) :
            c,t = answer.pop() 
            if c == 'undo' : 
                recursive_undo(temp,answer,0)
            temp2.append((c,t))
        temp.append(temp2[:])

        answer.append((command[0],command[2]))
    # print(answer, temp)
ret = ''
for ans in answer : 
    if ans[0] != 'undo':
        ret+=ans[0]
print(ret)

"""
7
type a 1
type b 2 
type c 3
type d 5
undo 3 6 
undo 2 7
undo 3 8
"""