
def change(left,right): 
    maxi = 0 
    maxi_index = 0
    maxi_count = 0 
    ret = False 
    for r in range(right,left,-1):
        if num[r] == 9 : 
            maxi_index = r 
            maxi = 9 
            break 
        if num[r] > maxi : 
            maxi_index = r 
            maxi = num[r]
            maxi_count = 0 
        elif num[r] == maxi:
            maxi_count +=1 
    small = num[left]
    small_index= left
    for m in range(maxi_count,-1,-1): 
        if num[left+m] < small:
            small = num[left+m]
            small_index = left+m
    if small_index != left :
        ret = True 
    left= small_index
    
    if num[left] > maxi : 
        if left+1 >= right : 
            num[right-1],num[right] = num[right],num[right-1]
        else: 
            change(left+1,right)
    elif num[left] == maxi : 
        while left < maxi_index and num[left]!=maxi:
            left+=1  
        if left == maxi_index : 
            if left+1 >= right:
                num[right-1],num[right] = num[right],num[right-1]
            else: 
                change(left+1,right)
    else: 
        num[left],num[maxi_index] = num[maxi_index], num[left]
    return ret 

tc = int(input())
for t in range(1,tc+1):
    num,cnt = input().split()
    num = list(map(int,str(num)))
    cnt = int(cnt)
    left = 0 
    right = len(num) -1 
    optim_num = sorted(num,reverse=True)
    duple = False 

    for n in num : 
        if num.count(n) >= 2:
            duple = True 
            break 
    for c in range(cnt): 
        if num == optim_num : 
            if duple : 
                break 
            else : 
                # change(right-1,right)
                if (cnt - c)%2 == 1 :
                    num[right],num[right-1] = num[right-1],num[right]
                break 
        if change(left,right):
            left-=1
        left+=1 
        print(num)
    num = ''.join(map(str,num))
    print(f"#{t} {num}")
