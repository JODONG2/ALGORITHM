tc = int(input())
def mix(num,visit,cnt,len_num,n):
    if cnt == len_num : 
        compare = ''
        for v in visit:
            compare+= num[v]
        return int(compare)%n == 0 and int(compare)//n >= 2 
    for i in range(len_num): 
        if not i in visit: 
            visit.append(i) 
            if mix(num,visit,cnt+1,len_num,n):
                return True 
            visit.pop()
    return False
for t in range(1,tc+1):
    num = list(input())
    len_num = len(num)
    if mix(num,[],0,len_num,int(''.join(num))):
        print(f"#{t} possible")
    else:
        print(f'#{t} impossible')