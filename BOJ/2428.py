
def bin_search(start,end,hw_list,n): 
    answer =0 
    for index in range(n):
        limit_size = hw_list[index]
        start = index +1
        end = n 
        while start<end: 
            mid = (start+end)//2
            if hw_list[mid]*0.9 <= limit_size :
                start = mid+1 
            elif hw_list[mid]*0.9 > limit_size : 
                end = mid
        answer += end - index - 1
    return answer 


if __name__ =="__main__":
    n = int(input()) 
    hw_list = list(map(int,input().split()))

    hw_list.sort()
    print(bin_search(0,n,hw_list,n))
    print(hw_list)


"""

5
1 1 1 1 1

2
2 1
"""