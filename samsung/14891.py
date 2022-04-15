from collections import deque 

dir_change={1:-1, -1:1} 

def input_data(): 
    wheel = [deque(map(int,input())) for _ in range(4)] 
    spin_cnt = int(input()) 
    spin = [list(map(int,input().split())) for _ in range(spin_cnt)]
    return wheel, spin_cnt, spin 

def point(wheel):
    point = 1 
    total = 0
    for w in wheel : 
        total += w[0]*point 
        point *=2
    return total 

def spin_r (wheel, wheel_num, dir):
    wheel_r= wheel[wheel_num][2]
    spin_wheel(wheel[wheel_num], dir)
    if wheel_num+1 < 4 and wheel[wheel_num+1][6] != wheel_r:
            spin_r(wheel,wheel_num+1,dir_change[dir])

def spin_l (wheel, wheel_num, dir):
    wheel_l = wheel[wheel_num][6] 
    spin_wheel(wheel[wheel_num], dir)
    if wheel_num-1 >= 0 and wheel[wheel_num-1][2] != wheel_l :
        spin_l(wheel,wheel_num-1, dir_change[dir])

def spin_wheel (wheel,dir):
    if dir == 1 : 
        wheel.appendleft(wheel.pop())
    elif dir == -1:
        wheel.append(wheel.popleft())

def spin (wheel , spins):
    for spin in spins : 
        wheel_num,dir = spin[0]-1, spin[1]
        wheel_r, wheel_l = wheel[wheel_num][2], wheel[wheel_num][6]
        spin_wheel(wheel[wheel_num], dir)
        if wheel_num+1 < 4 and wheel[wheel_num+1][6] != wheel_r:
            spin_r(wheel,wheel_num+1,dir_change[dir])
        if wheel_num-1 >=0 and wheel[wheel_num-1][2] != wheel_l :
            spin_l(wheel,wheel_num-1,dir_change[dir])
        
if __name__ =="__main__":
    wheels, spin_cnt, spins = input_data() 
    spin(wheels,spins)
    print(point(wheels))
