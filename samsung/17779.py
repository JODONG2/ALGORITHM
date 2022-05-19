"""
기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
다음 칸은 경계선이다.
(x, y), (x+1, y-1), ..., (x+d1, y-d1)
(x, y), (x+1, y+1), ..., (x+d2, y+d2)
(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
(x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

5 ≤ N ≤ 20
1 ≤ A[r][c] ≤ 100
"""
import sys 
n = int(sys.stdin.readline()) 
city = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def count_people(x,y,d1,d2): 
    right_x, right_y = x+d2, y+d2 
    left_x, left_y = x+d1,y-d1 
    under_x,under_y = x+d2+d1, y+(d2-d1)
    if right_x < n and right_y <n and left_x <n and 0<=left_y and under_x<n and 0<=under_y<n :
        div_city = [0 for _ in range(5)]
        ry,ly = y,y
        for i in range(n): 
            templ = i 
            tempr = i 
            for j in range(n):
                if i < left_x and j <= ly :
                    div_city[0] += city[i][j]
                    # print(1,i,j)
                    if left_y < ly and i >= x and templ == i: 
                        ly -= 1
                        templ = -1 
                elif i <= right_x and (j > ry ):#or (ry == n-1 and j == n-1)) : 
                    div_city[1] += city[i][j] 
                    # print(2,i,j)
                    if right_y > ry and i >= x and tempr == i:
                        tempr = -1 
                        ry += 1
                elif left_x<= i and (j < ly):#or (ly == 0 and i != left_x)):# or (ly == 0 and j == 0)): 
                    div_city[2] += city[i][j] 
                    # print(3,i,j)
                    if under_y > ly and i > left_x and templ == i:
                        ly += 1 
                        templ = -1 
                elif right_x < i and j >= ry : 
                    # print(4,i,j)
                    div_city[3] += city[i][j] 
                    if under_y < ry and i > right_x and tempr == i: 
                        ry -= 1 
                        tempr = -1 
                else : 
                    # print(5,i,j)
                    div_city[4] += city[i][j]
        # print(div_city,x,y,d1,d2,max(div_city)-min(div_city) )
        return True, max(div_city)-min(div_city)
    else : 
        return False, float('inf')
if __name__ =="__main__":
    x,y,d1,d2 = 1,2,1,1
    answer = float('inf')
    for x in range(n-2): 
        for y in range(1,n-1):
            for d1 in range(1, n-1):
                for d2 in range(1,n-1): 
                    check, num = count_people(x,y,d1,d2)
                    if check :
                        answer = min(answer,num) 
    print(answer)
    # x,y,d1,d2 = 2,4,2,1
    # count_people(x,y,d1,d2)
#5 6 6 7 8 7 8 9 8 9 1  -> 74 
#1 2 3 1 2 3 4 1 2 3 4 5 2 3 4 5 6 -> 51 

"""
6
1 2 3 4 1 6
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9
18

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

6
5 5 5 5 5 5
5 5 5 5 5 5
5 5 5 5 5 5
5 5 5 5 5 5
5 5 5 5 5 5
5 5 5 5 5 5

5
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5

4
5 5 5 5
5 5 5 5
5 5 5 5
5 5 5 5
"""