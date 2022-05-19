#x1y1 x2y2
#L = box_list 
#N = box_cnt 
from collections import deque 
def check(box,box2): 
    x1,y1,x2,y2 = box
    x3,y3,x4,y4 = box2
    if (x1<=x3<=x2 and y2<=y3<=y1) or (x1<=x4<=x2 and y2<=y4<=y1):
        return False
    elif x3<=x1<=x4 and y4<=y1<=y3 or (x3<=x2<=x4 and y4<=y2<=y3): 
        return False 
    return True 
    
def move(index,box,cnt,box_list,box_cnt) : 
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    q = deque() 
    q.append([box[0],box[1],box[2],box[3],0,[]])
    count = float("inf")
    result = []
    while q : 
        x1,y1,x2,y2,cnt,already = q.popleft()
        if count < cnt : 
            break
        if cnt >= 20 : 
            break
        for px,py in zip(dx,dy): 
            x1,x2 = x1+px, x2+px 
            y1,y2 = y1+py, y2+py
            succ = False
            for i in range(box_cnt):
                if i == index: 
                    continue
                if check([x1,y1,x2,y2],box_list[i]):
                    succ = True 
            if succ : 
                result = [x1,y1,x2,y2,cnt]
                return result                     
            else:
                if not [x1,y1,x2,y2] in already :
                    already.append([x1,y1,x2,y2])
                    q.append([x1,y1,x2,y2,cnt+1,already])
    return result 
        

def solution(N, L):
    answer = 1
    box_cnt = N 
    box_list = L
    for box in box_list:
        if len(box)==2 : 
            box*=2
    #box_list.sort(key=lambda x: abs(x[2]-x[0])+abs(x[3]-x[1]))
    box_list.sort(key=lambda x: [x[0],x[2]-x[0],x[1],x[3]-x[1]])
    for b in range(box_cnt) :
        for b2 in range(b+1, box_cnt):
            ch = check(box_list[b],box_list[b2]) # 겹치는게 있으면 False 
            if not ch:
                print(ch)
                result = move(b,box_list[b],0,box_list,box_cnt)
                box_list[b] = result[:4]
                answer += result[4]
                
    return answer
print(solution(3, [[5,7,6,6],[3,9,5,4],[8,2,7,6]]))
print(solution(3, [[5,7,6,6],[3,9,5,4],[6,6]]))