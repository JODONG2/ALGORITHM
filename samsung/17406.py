import sys 

def input_data():
    n,m,cnt = map(int,sys.stdin.readline().split())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    commands = [list(map(int,sys.stdin.readline().split())) for _ in range(cnt)] #-1해줘야됨
    return n,m,arr,commands,cnt

def spin(arr,r,c,s):
    r-=1 
    c-=1 
    while s!= 0 :
        temp1 = arr[r+s][c-s]
        temp2 = arr[r-s][c+s]
        temp3 = arr[r+s][c+s]
        for i in range(c+s,c-s,-1):
            arr[r-s][i] = arr[r-s][i-1] 
        for i in range(r+s,r-s+1,-1):
            arr[i][c+s] = arr[i-1][c+s] 
        arr[r-s+1][c+s] = temp2

        for i in range(c-s,c+s-1): 
            arr[r+s][i] = arr[r+s][i+1]
        arr[r+s][c+s-1] = temp3 

        for i in range(r-s,r+s) : 
            arr[i][c-s] = arr[i+1][c-s]
        arr[r+s-1][c-s] = temp1
        s-=1

def shuffle(arr,commands,cnt,used,answer):
    if len(used) == cnt : 
        ret = answer
        for a in arr:
            ret= min(ret, sum(a)) 
        return ret 

    for i in range(cnt): 
        if not i in used : 
            used.append(i)
            temp = [a[:] for a in arr] 
            spin(temp,commands[i][0],commands[i][1],commands[i][2])
            answer = min(answer,shuffle(temp,commands,cnt,used,answer))
            used.pop()
    return answer 


if __name__ =="__main__":
    n,m,arr,commands,cnt = input_data()
    print(shuffle(arr,commands,cnt,[],float('inf')))
    
    

"""
5 6 1
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2

5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

5 6 1 
1 2 3 4 5 6
7 8 9 10 11 12 
13 14 15 16 17 18 
19 20 21 22 23 24 
25 26 27 28 29 30 
3 4 1 

3 3 1 
1 2 3
4 5 6
7 8 9 
2 2 1
"""