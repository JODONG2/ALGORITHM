def input_data():
    N,M,money = map(int,input().split()) 
    friends = list(map(int,input().split()))
    connections = [list(map(int,input().split())) for _ in range(M)]
    return N,M,money,friends,connections


def Find(x:int, parent,friends): 
    if parent[x] == x:
        return x
    parent[x] = Find(parent[x],parent,friends)
    if friends[x] > friends[parent[x]]:
        friends[x] = friends[parent[x]]
    else : 
        friends[parent[x]] = friends[x]
    # print(parent,friends)
    return parent[x]

def merge(x,y,parent,friends):
    x = Find(x,parent,friends)
    y = Find(y,parent,friends) 
    if (x!=y):
        parent[y] = x 

def is_union(x,y,parent,friends):
    x=Find(x,parent,friends)
    y=Find(y,parent,friends)
    return x==y

def make_friends (N,M,money,friends,connections):
    sns = [i for i in range(N)]
    # print(sns)
    for connection in connections :
        mini = min(connection[0]-1, connection[1]-1)
        maxi = max(connection[0]-1 , connection[1]-1)
        merge(mini, maxi, sns,friends)
    
    for i in range(1):
        for j in range(N):
            is_union(i,j,sns,friends)
    sns = set(sns)
    answer = 0 
    for pay in sns : 
        answer+=friends[pay]
    if answer<=money:
        return answer
    else :
        return "Oh no"
        
if __name__ == "__main__":
    print(make_friends(*input_data()))

"""
5 3 20
10 20 20 10 30
1 3
2 4
5 4

답 : 20

5 1 1000
1 2 3 4 5
1 4

11

5 3 20
10 20 20 10 30
1 3
2 4
5 4


5 4 20
1 30 30 30 30
1 5
2 3
3 4
4 5


5 4 20
1 30 30 30 30
1 5
2 3
3 4
4 5



"""