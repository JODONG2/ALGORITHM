import sys

num = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

round = int(sys.stdin.readline())

lim = [list(map(int,sys.stdin.readline().split())) for _ in range (round)]
limi = []
for li in lim:
    for l in li:
        limi.append(l)
start = limi.index(max(limi))

print(limi)