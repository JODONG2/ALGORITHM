
def input_data():
    size = int(input())
    position = [-1,-1]
    row = 0 
    boxes = [] 
    for _ in range(size):
        boxes.append(list(input()))
        if "#" in boxes[-1] and position ==[-1,-1]:
            position = [row,boxes[-1].index("#")]
        row+=1 
    return size,boxes,position

if __name__ =="__main__":
    test_cases = int(input()) 
    for test_case in range(1, test_cases+1):
        size, boxes, position = input_data()
        rect = 0
        x,y = position
        answer = "yes"
        while y + rect < size and boxes[x][y+rect] == "#":
            boxes[x][y+rect] = "."
            rect+=1

        for px in range(1,rect):
            for py in range(rect): 
                if boxes[x+px][y+py] == "#" :
                    boxes[x+px][y+py] = "."
                else :
                    answer = "no"
        for box in boxes :
            if "#" in box : 
                answer = "no" 
        print(f"#{test_case} {answer}")
"""
3
3
...
.##
.##
4
#..#
....
....
#..#
5
.....
.###.
.###.
.###.
.....
"""
