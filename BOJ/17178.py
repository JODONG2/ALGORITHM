#줄서기 https://www.acmicpc.net/problem/17178
line_num = int(input())
line,seq,wait = [],[],[]

for _ in range(line_num):
    line.append(input().split())
    for ticket in line[-1]:
        seq.append(ticket)

seq.sort(key = lambda x : (x[0], int(x[2:])), reverse = True) 
# str로 역순 정렬하면 'A-401', 'A-4001', 'A-4', 'A-102'
# 위와 같이 역순 정렬해야 'A-4001', 'A-401', 'A-102', 'A-4'
for line_n in line:
    for tick in line_n:
        wait.append(tick)
        while((wait) and (wait[-1] == seq[-1])):
                del seq[-1]
                del wait[-1]
if wait :
    print("BAD")
else:
    print("GOOD")
