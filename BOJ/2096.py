import sys 
n = int(sys.stdin.readline()) 
before_max = [0,0,0]
before_min = [0,0,0]
for i in range(n): 
    x,y,z = map(int,sys.stdin.readline().split())
    if i == 0 : 
        before_max = [x,y,z]
        before_min = [x,y,z]
        continue 
    m1,m2,m3 = [before_max[0]+x,before_max[1]+x],[before_max[i]+ y for i in range(3)],[before_max[1]+z, before_max[2]+z]
    M1,M2,M3 = [before_min[0]+x,before_min[1]+x],[before_min[i]+ y for i in range(3)],[before_min[1]+z, before_min[2]+z]
    before_max[0] = max(*m1) 
    before_max[1] = max(*m2)
    before_max[2] = max(*m3) 
    before_min[0] = min(*M1)
    before_min[1] = min(*M2)
    before_min[2] = min(*M3)
print(max(before_max),min(before_min))
        
    