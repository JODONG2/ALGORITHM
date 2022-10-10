
def is_in_dict(char, dict):
    if dict.get(char.lower()) or dict.get(char.upper()): 
        return True 
    else : 
        return False 

cnt = int(input())
dic = {}
for _ in range(cnt):
    string = input().split()
    succ = False 
    answer = ""
    for s in string:
        if is_in_dict(s[0],dic) or succ : 
            answer+=s 
        else :
            dic[s[0].lower()] = 1 
            dic[s[0].upper()] = 1 
            succ = True 
            answer += "["+s[0]+"]" +s[1:]
        answer += ' '
    if succ :
        print(answer)
    if not succ : 
        answer = ""
        done = False 
        for s in string :
            for s2 in s : 
                if done : 
                    answer += s2 
                elif is_in_dict(s2,dic) : 
                    answer+=s2
                else : 
                    dic[s2.lower()] = 1 
                    dic[s2.upper()] = 1 
                    done = True 
                    answer += '['+s2+']'
            answer += ' '
        print(answer )
        

            
            