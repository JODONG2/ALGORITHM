def rotate(road,n): 
    road2 = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n): 
            road2[j][i] = road[i][j] 
    return road2 

def road_check(line,n,l) -> bool :
    check = [0 for _ in range(n)]
    for i in range(1,n):
        if line[i] == line[i-1] :
            continue 

        elif line[i] - line[i-1] == -1 : # 내리막길
            for j in range(l):
                if i+j < n and line[i+j] == line[i] and not check[i+j] :
                    check[i+j] = 1
                    continue 
                else :
                    return False
            i += l
            continue

        elif line[i] - line[i-1] == 1 : #오르막길 
            for j in range(1,l+1): 
                if i-j>=0 and line[i-j] == line[i-1] and not check[i-j] :
                    check[i-j] = 1 
                    continue 
                else :
                    return False
            continue

        else:
            return False 
    return True 

def find_path(n,l,road): 
    road2 = rotate(road,n)
    ans =0
    for i in range(n):
        if road_check(road[i], n, l) : ans += 1
        if road_check(road2[i], n,l) : ans += 1
    return ans 

if __name__ == "__main__":
    n,l = map(int,input().split()) 
    road = [list(map(int,input().split())) for _ in range(n)] 
    print(find_path(n,l,road))
