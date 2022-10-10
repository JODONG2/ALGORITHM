def find_max_min (num,len_num):
    check_mini = True 
    check_maxi = True
    minimum = num 
    maximum = num
    for i in range(len_num):
        mini,mini_index = num[i], i
        maxi, maxi_index = num[i], i
        for j in range(i,len_num):
            if mini > num[j] and i != 0  and check_mini:
                mini,mini_index = num[j], j 
            elif mini >num[j] and i==0 and check_mini:
                if num[j] != '0' : 
                    mini,mini_index = num[j], j
            elif num[i] != mini and check_mini and mini >= num[j] : 
                  mini,mini_index = num[j], j 
            if maxi <= num[j] and check_maxi :
                if i == 0 and maxi == num[j] :
                    continue 
                if i != 0 and maxi == num[i] : 
                    continue 
                maxi, maxi_index = num[j],j
        if mini_index != i and check_mini:
            check_mini = False
            minimum = [ n for n in num ]
            minimum[i],minimum[mini_index] =  minimum[mini_index], minimum[i]
        if maxi_index != i and check_maxi:
            check_maxi = False 
            maximum = [ n for n in num ]
            maximum[i],maximum[maxi_index] = maximum[maxi_index], maximum[i]
        if not check_mini and not check_maxi:
            break

    return ''.join(minimum), ''.join(maximum)
    
if __name__ == "__main__":
    T = int(input()) 
    for t in range(1,T+1):
        answer = f"#{t} "
        num = input()
        len_num = len(num) 
        minimum, maximum = find_max_min(num,len_num)
        answer += minimum + " "
        answer += maximum 
        print(answer)

   
"""
15
911
119
101
1520
11110
11520
10101
12504
9450
99450
1052
10052
2510
21320
3210
"""

"""
T = int(input())
 
for t in range(T):
    N = list(input())
    sett = {''.join(N)}
 
    for i in range(len(N) - 1):
        for j in range(i, len(N)):
            if (i == 0 and N[j] != '0') or i > 0:
                N[i], N[j] = N[j], N[i]
                sett.add(''.join(N))
                N[i], N[j] = N[j], N[i]
 
    print(f'#{t+1} {min(sett)} {max(sett)}')
"""