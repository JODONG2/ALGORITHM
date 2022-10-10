n = int(input())
graph = [0 for _ in range(n+1)] 
for job_num in range(1,n+1): 
    infor = list(map(int,input().split())) 
    time,need_cnt,need = infor[0],infor[1],infor[2:]
    maxi_need = 0
    for ne in need: 
       maxi_need = max(graph[ne], maxi_need) 
    graph[job_num] = maxi_need+time
print(max(graph))

"""
7
5 0
3 0
6 0
1 0
8 0
4 0
2 0
"""