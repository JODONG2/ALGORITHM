"""
9
1 2 3 4
2
3 5
4 6
5 7 8 9
6 8 9
7
8
9
"""
import sys 
from collections import deque 

answer = float('inf')
def optim(now,check,start):
    

students = int(sys.stdin.readline())
graph = [[] for _ in range(students+1)] 
for i in range(1,students+1):
    pn = list(map(int,sys.stdin.readline().split()))
    graph[i] = pn[1:] 
check = [True for _ in range(students+1)]
start = deque([1])