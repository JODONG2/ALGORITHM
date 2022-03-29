from collections import deque 
def input_data():
    n = int(input())
    city = [list(map(int,input())) for _ in range(n)]
    return n, city 

def search(n,city):
    check = [[True for _ in range(n)] for _ in range(n)]
    answer = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1 and check[i][j] :
                check[i][j] = False 
                q = deque() 
                cnt = 1 
                q.append((i,j)) 
                while q : 
                    x,y = q.popleft()
                    for px,py in zip(dx,dy):
                        nx,ny = x+px, y+py 
                        if 0<= nx < n and 0<= ny < n and city[nx][ny] and check[nx][ny] : 
                            check[nx][ny] = False
                            cnt+=1
                            q.append((nx,ny))
                answer.append(cnt)
    return len(answer),sorted(answer)
    


if __name__ == "__main__":
    n,city = input_data() 
    len_answer, answer = search(n,city)
    print(len_answer)
    for a in answer:
        print(a)