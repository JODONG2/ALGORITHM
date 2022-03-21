from collections import deque 
if __name__ == "__main__":
    f,s,g,u,d = map(int, input().split())
    q = deque() 
    dirs = [u,-d] 
    visit= [-1 for _ in range(0,f+1)]
    visit[s] = 0 
    q.append(s) 
    while q : 
        pos = q.popleft()
        for dir in dirs:
            new_pos = pos+dir 
            if 1<=new_pos<=f and visit[new_pos] == -1 : 
                visit[new_pos] = visit[pos]+1 
                q.append(new_pos)
        if visit[g] != -1 : 
            break 
    answer = visit[g] if visit[g] != -1 else "use the stairs"
    print(answer)

