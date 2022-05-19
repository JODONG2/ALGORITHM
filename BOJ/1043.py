import sys 
from collections import deque 
n,m = map(int,sys.stdin.readline().split())
already_know = list(map(int,sys.stdin.readline().split()))[1:]
party_people = [list(map(int,sys.stdin.readline().split()))[1:] for _ in range(m)]
q = deque(already_know)
party_list = [True for _ in range(m)] 
while q : 
    human = q.popleft() 
    for i,people in enumerate(party_people):
        if not party_list[i] : 
            continue
        if human in people : 
            party_list[i] = False 
            for p in people : 
                if not p in already_know:
                    already_know.append(p)
                    q.append(p)
answer = 0 
for party in party_list:
    if party:
        answer+=1 
print(answer)

    
