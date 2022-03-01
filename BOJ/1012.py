import sys 
from collections import deque 

if __name__=="__main__":
    test_case = int(input()) 
    for _ in range(test_case):
        M,N,cnt = map(int, sys.stdin.readline().split())
        position = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]
        position.sort(key= lambda x: [x[0],x[1]])
        position = deque(position)
        answer = 1
        #print(position)
        groups = [[position.popleft()]]
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while position : 
            pos = position.popleft()
            #print(groups,"<- group pos ->" ,pos )
            is_in = False
            cnt= []
            for px,py in zip(dx,dy):
                for g in range(len(groups)):
                    if [pos[0]+px,pos[1]+py] in groups[g]:
                        cnt.append(g)
                        #groups[g].append(pos)
                        is_in = True
                        break
            if is_in :
                cnt = list(set(cnt))
                if len(cnt) > 1: 
                    temp = [pos]
                    temp2=[]
                    for i in cnt:
                        temp += groups[i]
                    cnt.sort(reverse = True)
                    for c in cnt :
                        del groups[c]
                    
                    groups.append(temp)

                elif len(cnt) == 1 : 
                    groups[cnt[0]].append(pos)
                
            else : 
                groups.append([pos])
        #for i,group in enumerate(groups) : 
        #    print(i,group)
        print(len(groups))
"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

1   
3 3 7
0 0
0 1
0 2
1 0
1 2
2 0
2 2

 2
15 15 21
0 3
0 12
1 12
1 14
2 1
2 10
2 11
3 6
4 1
5 4
6 10
6 13
7 7
9 3
9 4
10 3
10 10
10 11
12 1
12 9
14 14
15 15 80
0 0
0 1
0 4
0 10
1 2
1 7
1 10
1 12
1 13
2 2
2 3
2 7
3 2
3 4
3 6
3 8
3 11
3 14
4 0
4 1
4 2
4 5
4 6
4 7
4 8
4 11
4 12
4 14
5 0
5 2
5 4
5 7
5 8
5 10
5 11
5 13
5 14
6 5
6 10
6 12
6 13
6 14
7 1
7 9
7 12
7 13
8 2
8 4
8 8
8 9
8 12
8 13
9 0
9 3
9 5
9 11
10 2
10 3
10 5
10 9
10 10
11 8
11 9
11 11
11 12
11 13
12 3
12 13
12 14
13 1
13 4
13 7
13 9
13 10
13 13
14 0
14 5
14 7
14 8
14 13



1
15 15 80
0 0
0 1
0 4
0 10
1 2
1 7
1 10
1 12
1 13
2 2
2 3
2 7
3 2
3 4
3 6
3 8
3 11
3 14
4 0
4 1
4 2
4 5
4 6
4 7
4 8
4 11
4 12
4 14
5 0
5 2
5 4
5 7
5 8
5 10
5 11
5 13
5 14
6 5
6 10
6 12
6 13
6 14
7 1
7 9
7 12
7 13
8 2
8 4
8 8
8 9
8 12
8 13
9 0
9 3
9 5
9 11
10 2
10 3
10 5
10 9
10 10
11 8
11 9
11 11
11 12
11 13
12 3
12 13
12 14
13 1
13 4
13 7
13 9
13 10
13 13
14 0
14 5
14 7
14 8
14 13
"""