from collections import deque 
operation = input() 
q = deque() 
def pl(x,y):
    return x+y 
def mu(x,y):
    return x*y 
def di(x,y):
    return x//y 
def mi(x,y):
    return x-y 
for op in operation: 
    if op.isdigit(): 
        q.append(int(op)) 
    if op == ')':
        temp = ''
        while q[-1] != '(':
            temp = q.pop()+temp
        q.pop() 
        