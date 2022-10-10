
tc = int(input())
for t in range(1,tc+1):
    n,d = map(int,input().split()) 
    answer = n//(2*d +1) + 1 if n%(2*d+1) != 0 else n//(2*d +1)
    print(f"#{t} {answer}")