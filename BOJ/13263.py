import sys 
from collections import deque 
#TODO: NxN 행렬 높이 max번 반복 -> 최대 N * max(높이)
if __name__ == "__main__": 
    N = int(input()) 
    height= deque(list(map(int,sys.stdin.readline().split())))
    cost = deque(list(map(int, sys.stdin.readline().split())))

    dp= [[0 for _ in range(N)] for _ in range(N)] 
    



"""

6
1 2 3 10 20 30
6 5 4 3  2  0

  12 18 60 120 180 
2 12 27 62 112 162

3 26 18 58 98 138

4 64 69 60 120 150 

"""
