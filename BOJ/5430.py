import sys 
from collections import deque 
test_case = int(sys.stdin.readline())
answer =[]
for _ in range(test_case):
    # command = deque(list(sys.stdin.readline()))
    # len_arr = int(sys.stdin.readline())
    # arr = deque(list(map(int,sys.stdin.readline().lstrip('[').rstrip(']\n').split(','))))
    command = deque(list(input()))
    len_arr = int(input())
    input_str = input() 
    if input_str == "[]":
        arr = [] 
    else : 
        arr = deque(list(map(int,input_str.lstrip('[').rstrip(']\n').split(',')))) 
    R = False
    err = False
    for comm in command:
        #comm = command.popleft()
        if comm =="R":
            R = not R
        elif comm == "D":
            if not arr : 
                answer.append('error')
                err = True 
                break
            if R : 
                arr.pop()
            else : 
                arr.popleft() 
    if not arr :
        if not err :
            answer.append([])
        continue
    if R :
        arr.reverse()
        answer.append(list(arr))
    else : 
        answer.append(list(arr))
for ans in answer :
    print(''.join((str(ans).split())))
"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]


1
DDDD
4
[1,2,3,4]


3
D
0
[]
R
0
[]
R
0
[]
"""