import re 

p = re.compile("(100+1+|01)+")
input_str = input()
m = p.fullmatch(input_str)

if m!= None :
    print("SUBMARINE")
else:
    print("NOISE")
