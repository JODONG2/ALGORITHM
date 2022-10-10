
N = [-2,-1,1,2]
for t in range(1,11):
    len_height = int(input())
    answer = 0 
    height = list(map(int,input().split()))
    index= 2
    while index<len_height-2:
        h = height[index]
        check = True 
        n_height = 0
        for n in N:
            if height[index+n] >= h : 
                check= False
                if n > 0 :
                    index += n
                else: 
                    index+=1 
                break
            else: 
                n_height = max(n_height, height[index+n])
        if check : 
            answer += (h - n_height) 
            index+=3 
    print(f"#{t} {answer}") 