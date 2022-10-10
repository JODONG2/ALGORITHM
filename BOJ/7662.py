import heapq 
import sys 
tc = int(sys.stdin.readline())
for _ in range(tc):
    min_heap = []
    max_heap = [] 
    cnt_command = int(sys.stdin.readline())
    already_out = [False for _ in range(cnt_command)]
    for ident in range(cnt_command):
        command,num = sys.stdin.readline().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap,(num,ident))
            heapq.heappush(max_heap, (-num,num,ident))
        elif command =='D':
            if not min_heap or not max_heap:
                continue 
            if num == 1:
                _,_,iden = heapq.heappop(max_heap)
                while max_heap and already_out[iden]:
                    _,_,iden = heapq.heappop(max_heap)
                already_out[iden] = True 
            elif num ==-1 :
                _,iden = heapq.heappop(min_heap)
                while min_heap and already_out[iden]:
                    _,iden = heapq.heappop(min_heap)
                already_out[iden] = True 
    if min_heap and max_heap: 
        mini, ide = heapq.heappop(min_heap)
        while min_heap and already_out[ide] :
            mini,ide = heapq.heappop(min_heap)
        if already_out[ide] : 
            print("EMPTY")
            continue
        _,maxi,ide = heapq.heappop(max_heap)
        while max_heap and already_out[ide]:
            _,maxi,ide = heapq.heappop(max_heap)
        print(maxi, mini)
    else: 
        print("EMPTY")