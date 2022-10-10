

def solution(A):
    # print(A)
    len_A = len(A) 
    bit =0
    ans = 0 
    for a in A: 
        bit |= 1<<a 
        fail = False 
        comp = (1<<(a+1)) -1 
        print(bit, comp)
        if bit == comp : 
            ans+=1
        # for i in range(1,a+1) : 
        #     if not (bit & (1<<i)) :
        #         print(bit, 1<<i)
        #         fail = True 
        #         break 
        # if not fail : 
        #     ans +=1
    
    print(ans)

solution( [2, 1, 3, 5, 4])
solution( [2, 1, 3, 4, 5])
solution( [1,3,4,2,5])