T = int(input()) 
for t in range(1,T+1) : 
    life = 8
    results = input() 
    answer = f"#{t}"
    for result in results : 
        if result == 'x' : 
            life -= 1 
            if life == 0 : 
                break 
    if life == 0 : 
        answer+= "NO"
    else :
        answer+="YES"
    print(answer)

"""
3
oxoxoxoxoxoxoxo
x
xxxxxxxxxxxx
"""