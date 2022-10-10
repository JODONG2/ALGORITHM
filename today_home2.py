def solution(beds, tables, cost):
    answer = float("inf")
    for bed in beds :
        for table in tables :
            mini = float("inf")
            bx,by,cos_bed = bed[0],bed[1],bed[2]
            tx,ty,cos_tab = table[0],table[1],table[2]
            mini = min((bx+tx)*max(by,ty), (bx+ty)*max(by,tx), (by+tx)*max(bx,ty), (by+ty)*max(bx,tx))
            answer = min(mini*cost + cos_tab + cos_bed, answer)

    return answer