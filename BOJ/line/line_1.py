from typing import List
def solution(queries: List[List[int]]) -> int:
    answer = 0
    arr = [[1,0] for _ in range(1000)]
    for idx, cnt in queries : 
        if arr[idx][1] == 0 :
            arr[idx][1] += cnt
            while arr[idx][0] < arr[idx][1] : arr[idx][0] *= 2
        else : 
            if arr[idx][0]< arr[idx][1] + cnt: 
                answer += arr[idx][1]
            arr[idx][1] += cnt
            while arr[idx][0] < arr[idx][1] : arr[idx][0] *= 2 
    return answer