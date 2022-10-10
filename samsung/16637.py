answer = -float("inf")
def dfs(number,pmmd,index):
    global answer
    len_pmmd = len(pmmd)
    compare = number[0] 
    for i in range(len_pmmd):
        compare = calculate(compare,number[i+1],pmmd[i])
    if answer < compare : 
        answer = compare

    for i in range(len_pmmd):
        if index - i<=1 : 
            continue 
        num1,num2 = number[i],number[i+1] 
        number[i] = calculate(num1,num2,pmmd[i])
        temp = [number[j] for j in range(len(number)) if j != i+1]
        temp2 = [pmmd[j] for j in range(len_pmmd) if j != i]
        dfs(temp,temp2,i)
        number[i],number[i+1] = num1,num2
    
    
def calculate(num1,num2,op):
    if op == "+":
        return num1+num2
    elif op == "*":
        return num1*num2 
    elif op == "-":
        return num1-num2

len_command = int(input())
command = list(input())
number = [] 
pmmd = [] 
used = [0 for _ in range(len_command//2)]
for i in range(len_command):
    if i % 2 == 0 : 
        number.append(int(command[i]))
    else : 
        pmmd.append(command[i])
number_check = [True for _ in range(len_command//2 +1)]
dfs(number,pmmd,float('inf'))
print(answer)