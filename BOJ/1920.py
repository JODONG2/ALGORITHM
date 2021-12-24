N = int(input())
di = {}
input_num_list = list(map(int,input().split()))
for n in range(N):
    input_num = input_num_list[n]
    di[input_num] = input_num
M = int(input())
compare_num_list = list(map(int,input().split()))
for m in range(M):
    compare_num = compare_num_list[m]
    try:
        di[compare_num] 
        print(1)
    except:
        print(0)

