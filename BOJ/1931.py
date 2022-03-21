import sys 

if __name__ == "__main__": 
    n = int(input()) 
    time_table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    time_table.sort(key = lambda x: (x[1],x[0]))
    last_end = 0 
    answer = 0
    for start,end in time_table : 
        if last_end <= start : 
            answer+=1 
            last_end = end 
    print(answer)

