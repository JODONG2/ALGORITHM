def bin_search(hw, index, cnt):
    start = index + 1
    end = cnt 
    while (start < end):
        mid = (start+end)//2
        if hw[index] >= 0.9 * hw[mid] : 
            start = mid +1
        else: 
            end = mid
    return end - index - 1
if __name__=="__main__":
    cnt = int(input())
    hw_size = list(map(int,input().split()))
    hw_size.sort()
    answer = 0
    for index in range(cnt):
        answer += bin_search(hw_size, index , cnt)
    print(answer)