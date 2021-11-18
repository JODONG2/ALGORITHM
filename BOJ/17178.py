#줄서기 
line_num = int(input())
line,seq,wait = [],[],[]

for _ in range(line_num):
    line.append(input().split())
    for ticket in line[-1]:
        seq.append(ticket)

seq.sort(key = lambda x : (x[0], int(x[2:])), reverse = True)
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
