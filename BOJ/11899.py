# 괄호끼워넣기
stack = []
question = input()
for q in question:
    if q == '(':
        stack.append('(')
    elif q ==')':
        if stack and stack[-1] == '(' :
            stack.pop()
        else:
            stack.append(q)

print(len(stack))
