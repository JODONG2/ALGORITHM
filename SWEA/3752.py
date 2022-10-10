def permutation(answer):
    temp = set() 
    for i in range(n): 
        for p in answer:
            temp.add(p+num[i])
        answer = temp|answer
    return answer 
tc = int(input())
for t in range(1,tc+1):
    n = int(input())
    num = list(map(int,input().split()))
    visit = [True for _ in range(n)]
    answer = permutation(set([0]))
    print(f"#{t} {len(answer)}")