import re 
from collections import deque 
input_str = input()
pattern = "[0-9]+"
a = deque(re.split(pattern, input_str))
a.popleft()
a.pop()
print(a)
pattern = "[*/+-]"
b = deque(re.split(pattern, input_str))
print(b)

def mult(num1,num2):
    return num1* num2
def plus(num1,num2):
    return num1+num2
def minu(num1,num2):
    return num1-num2
def divi(num1,num2):
    return num1//num2

def cmd(num1,num2,comm):
    if comm == '*' : return mult(num1,num2)
    elif comm == '/' : 
        if num2 != 0 :
            return divi(num1,num2) 
        else : 
            return num1 
    elif comm == '+' : return plus(num1, num2)
    elif comm == '-' : return minu(num1,num2) 
    elif comm =='!' : return num1
priority = ['*','/'] 
b_left1, b_left2, b_right1, b_right2 = 0,0,0,0
a_left,a_right = '!','!'
cnt = 0 
result_right, result_left = 0,0
ans = 0 
if not a : 
    ans = b[0]
while a and b : 
    if a_left == '!':
        a_left = a.popleft() 
    if a_right =='!':
        a_right = a.pop()

    if(b_left1 == 0 and b_left2 == 0):
        b_left1 = int(b.popleft())
        if b :
            b_left2 = int(b.popleft()) 
        else :
            b_left2 = 0 

    if(b_right1 == 0 and b_right2 == 0):
        b_right1 = int(b.pop())
        if b : 
            b_right2 = int(b.pop())
        else : 
            b_right2 = 0 

    a_left_first = a_left in priority 
    a_right_first = a_right in priority 
    if not a  : 
        result_left = cmd(b_left1,b_left2,a_left)
        result_right = cmd(b_right1, b_right2, a_right) 
        print(result_left, result_right)
        a_ = a_left if not a_left != '!' else a_right
        ans = cmd(result_left,result_right,a_)
    elif (a_left_first and a_right_first) or (not (a_left_first or a_right_first)): 
        result_left = cmd(b_left1,b_left2,a_left)
        result_right = cmd(b_right1, b_right2, a_right) 
        if(result_left>=result_right):
            b.appendleft(result_left)
            b_left1 = 0 
            b_left2 = 0
            a_left = '!'
        else : 
            b.append(result_right)
            b_right1 = 0
            b_right2 = 0 
            a_right = '!' 
    elif a_left_first and not a_right_first : 
        result_left = cmd(b_left1,b_left2,a_left) 
        result_right = cmd(b_right1, b_right2, a_right) 

        b.appendleft(result_left) 
        b_left1 = 0 
        b_left2 = 0 
        a_left = '!' 
    else : 
        result_right = cmd(b_right1,b_right2,a_right)
        result_left = cmd(b_left1,b_left2,a_left) 

        b.append(result_right)
        b_right1 = 0 
        b_right2 = 0 
        a_right ='!'
    print(a)
    print(b)
    print(result_left, result_right,cnt)
    print(b_left1, b_left2, b_right1, b_right2)
    cnt+=1 
    if cnt == 10 :
        break 
print(ans)