time = int(input())
for t in range(1,time+1):
    N = int(input())
    answer = 0 
    i=0
    flag = True
    for _ in range(N):
        if i == 0 :
            answer += int(input()[int(N/2)])
            i+=1
            continue
        line = input()
        for j in range(int(N/2)-i, int(N/2)+i+1):
            answer += int(line[j])
        if i == int(N/2):
            flag = False
        if flag :
            i += 1 
        else:
            i -=1
    print (f"#{t} {answer}")

"""
1
5
14054
44250
02032
51204
52212 
"""
"""
1
5
12012
10001
00000
10001
12012
"""