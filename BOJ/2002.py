from collections import deque 
import sys 
cnt = int(sys.stdin.readline())
in_terminal = deque()
out_terminal = deque() 
sequence = [] 
for i in range(cnt) : 
    key = sys.stdin.readline()
    in_terminal.append(key)
for i in range(cnt): 
    out_terminal.append(sys.stdin.readline()) 
answer = 0 
while in_terminal :
    compare = in_terminal.popleft() 
    if compare in sequence:
        continue 
    while out_terminal :
        temp = out_terminal.popleft() 
        if temp == compare:
            break 
        answer +=1
        sequence.append(temp)
print(answer)


# in_terminal = {} 
# out_terminal = {} 
# key_list = [] 
# for i in range(cnt):
#     key = input()
#     in_terminal[key] = [i,key]
#     key_list.append(key)
# for i in range(cnt):
#     out_terminal[input()] = i 
# answer=0
# compare = 0 
# for key in key_list:
#     if in_terminal[key][0] + compare > out_terminal[key] :
#         answer+=1
#         compare += 1 
# print(answer)
"""
4
a
b
c
d
d
c
b
a


"""