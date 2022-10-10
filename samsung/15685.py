"""
0,0 -> 1,0 
0,0 -> 1,0 -> 1,-1
0,0 -> 1,0 -> 1,-1 -> 0,-1 -> 0,-2 
재귀 ? 
첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다. 
드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다. x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
"""

dir = [(1,0), (0,-1),(-1,0),(0,1)]

def curve(dragon,x,y,d,g,dir_list):
    #TODO: 커브 좌표 찍기 
    if g == -1 : 
        return dragon 
    if not dragon : 
        dragon.append((x,y))
        x += dir[d][0]
        y += dir[d][1]
        dragon.append((x,y))
        dir_list.append((d+1)%4)
        return curve(dragon,x,y,d,g-1,dir_list)
    else : 
        len_dir_list = len(dir_list)
        for i in range(len_dir_list-1, -1 ,-1):
            dragon.append((dragon[-1][0]+dir[dir_list[i]][0], dragon[-1][1]+dir[dir_list[i]][1]))
            dir_list.append((dir_list[i]+1)%4)
        return curve(dragon,x,y,d,g-1,dir_list)

def point(dragon_curve): 
    arr = [[0 for _ in range(101)] for _ in range(101)] 
    ret = 0 
    for dragon in dragon_curve: 
        for drago in dragon : 
            arr[drago[0]][drago[1]] = 1 
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1] : 
                ret +=1
    return ret 

if __name__ == "__main__":
    N = int(input()) 
    infor = [list(map(int,input().split()))for _ in range(N)]
    dragon_curve = [] 
    for info in infor: 
        dragon_curve.append(curve([], *info, []))
    print(point(dragon_curve))


"""
3
3 3 0 1
4 2 1 3
4 2 2 1
"""