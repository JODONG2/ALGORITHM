
def solution(rounds):
    answer = 0
    #참가자 abcd네사람 
    #return 규칙 어긴 횟수 
    #자기 자신 지목하면 안됨 
    #커플되면 다음 라운드에 같은 사람 지목하면 안됨 솔로만세 :)
    match = {"a":0, "b":1, "c":2, "d":3}
    before_round = [-1 for _ in range(4)]
    couple = [False for _ in range(4)]
    for roun in rounds:
        for i,love in enumerate(roun) : 
            if match[love] == i :
                answer+=1
                before_round[i] = -1
                continue
            else :
                if couple[i] and before_round[i] == match[love]:
                    answer+=1
                    before_round[i] = -1
                    continue 
            before_round[i] = match[love] 

        for i in range(4):
            if before_round[before_round[i]] == i:
                couple[i] = True
            else:
                couple[i] = False
    return answer

print(solution([['b','a','d','c'],['b','a','d','c'],['b','a','d','c']]))