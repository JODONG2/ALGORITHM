

n = int(input()) 
seq = list(map(int,input().split())) 
shu = list(map(int,input().split())) 
cards = [i%3 for i in range(n)]
origin = cards[:]
correct = [cards[i] for i in seq]
def shuffle(cards,shu):
    return [cards[i] for i in shu]
answer = 0 
while cards != correct : 
    answer+=1 
    cards = shuffle(cards,shu)
    if cards == origin :
        answer = -1 
        break
print(answer)
