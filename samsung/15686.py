"""

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
"""
n,m = map(int,input().split()) 
city = [list(map(int,input().split())) for _ in range(n)] 
home = [] 
chick = [] 
for i in range(n) : 
    for j in range(n): 
        if city[i][j] == 1 : 
            home.append((i,j))
        elif city[i][j] == 2 : 
            chick.append((i,j)) 


def dist(ch_list): 
    #TODO: 치킨 거리 최소 1 
    #TODO: |r1-r2| + |c1-c2| 중 작은값 합
    dist = 0
    for h in home: 
        mini = float("inf")
        for ch in ch_list : 
            mini = min(mini,abs(h[0] - ch[0]) + abs(h[1] - ch[1]))
        dist += mini 
    return dist 

def del_m(cnt, ch_list, ret,i): 
    #TODO: 살려둘 m개의 치킨집 
    #TODO: 남은 치킨집 개수 == cnt 
    #TODO: if cnt == m : return dist(home,chick)
    #TODO: 넣으면서 가기 123 -> 132 또하게 됨 
    if cnt == m :
        ret = min(ret, dist(ch_list)) 
        return ret 
    for index,c in enumerate(chick):
        if not c in ch_list and index > i: 
            ch_list.append(c)
            ret = del_m(cnt+1, ch_list, ret, index)
            del ch_list[-1]
    return ret
    

if __name__ == "__main__": 
    print(del_m(0,[],float("inf"),-1))

"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1

32
"""