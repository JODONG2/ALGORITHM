import sys 
city_cnt, ticket_value = map(int,sys.stdin.readline().split())
cities = {} 
for city in sys.stdin.readline().split():
    cities[city] = [] 

target_cnt = int(sys.stdin.readline())
target = sys.stdin.readline().split()
ticket_cnt = int(sys.stdin.readline())
for _ in range(ticket_cnt):
    sys.stdin.readline().split()

print(target)
print(cities)
