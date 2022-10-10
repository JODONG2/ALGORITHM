

if __name__ == "__main__":
    test_case = int(input())
    for tc in range(1,test_case+1) :
        N = int(input()) 
        hate_num = list(map(int,input())) 
        total = 1 
        for i in range(1,N+1): 
            total*=i 
            