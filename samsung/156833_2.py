
def input_data():
    n,m = map(int,input().split()) 
    #office = [list(map(int,input().split())) for _ in range(n)]
    office = [] 
    position = [] 
    for i in range(n) :
        office.append(list(map(int,input().split()))) 
        
    return n,m,office,position 

def show_u(n,m,office,position,view): 
    x,y = position[0], position[1]
    for i in range(x): 
        if office[i][y] != 6 : 
            view.add([i,y])
        elif office[i][y] == 6:
            view.add([i,y])
            break 
    return view 

def show_d(n,m,office,position,view):
    x,y = position[0],position[1] 
    for i in range(x,n):
        if office[i][y] != 6 :
            view.add([i,y]) 
        elif office[i][y] == 6:
            view.add([i,y]) 
            break 
    return view 

def show_r(n,m,office,position,view):
    x,y = position[0],position[1] 
    for i in range(y,m):
        if office[x][i] != 6 :
            view.add([x,i]) 
        elif office[x][i] == 6:
            view.add([x,i]) 
            break 
    return view

def show_l(n,m,office,position,view):
    x,y = position[0],position[1] 
    for i in range(y):
        if office[x][i] != 6 :
            view.add([x,i]) 
        elif office[x][i] == 6:
            view.add([x,i]) 
            break 
    return view 

def rotate_1(n,m,office,position):
    view_list  = [[] for _ in range(4)] 
    view_list[0]=(show_d(n,m,office,position,set()))
    view_list[1]=(show_u(n,m,office,position,set()))
    view_list[2]=(show_r(n,m,office,position,set()))
    view_list[3]=(show_l(n,m,office,position,set()))
    return view_list

def rotate_2(view_list): 
    view_list2 = []
    view_list2.append(view_list[0] + view_list[1])
    view_list2.append(view_list[2] + view_list[3]) 
    return view_list2 

def rotate_3(view_list): 
    view_list2 = [] 
    view_list2.append(view_list[0]+view_list[2])
    view_list2.append(view_list[0]+ view_list[3])
    view_list2.append(view_list[1]+view_list[2])
    view_list2.append(view_list[1]+view_list[3]) 
    return view_list2 

def rotate_4(view_list): 
    view_list2 = [] 
    view_list2.append(view_list[0]+view_list[2]+view_list[3])
    view_list2.append(view_list[1]+view_list[2]+view_list[3])
    view_list2.append(view_list[0] + view_list[1] + view_list[2])
    view_list2.append(view_list[1] + view_list[0] +view_list[3])
    return view_list2

def rotate_5(view_list):
    view_list2 = [] 
    view_list2.append(view_list[0]+view_list[1]+view_list[2]+view_list[3])
    return view_list2

def mini_area(n,m,office,positions):
    show = set()
    for i in range(5):
        for position in positions[i]:
            show_where = rotate_1(n,m,office,position)
            if i == 0 : 
                


if __name__ == "__main__":
    n,m,office,position = input_data() 
    print(position)


"""
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5

15
"""