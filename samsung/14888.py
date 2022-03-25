
def input_data(): 
    N = int(input())
    num_list = list(map(int,input().split()))
    operations = list(map(int,input().split())) 
    return N,num_list,operations


def find_max_min (num, num_list, operations, mini, maxi,string): 
    #print(string,num)
    if not num_list:
        if mini > num : 
            mini = num 
        if maxi < num : 
            maxi = num 
        #print(string+"=",num)
        return mini,maxi

    if operations[1] :
        operations[1] -=1 
        num1,num2  = find_max_min(num-num_list[0], num_list[1:],operations,mini,maxi, string+"-"+str(num_list[0]))
        mini=min(mini,num1) 
        maxi=max(maxi,num2)
        operations[1] +=1 

    if operations[3] :
        operations[3] -=1
        if num < 0 : 
            num2 = -(-num // num_list[0])
        else : 
            num2 = num//num_list[0]
        num1,num2= find_max_min(num2, num_list[1:], operations,mini,maxi,string+"%"+str(num_list[0]))
        mini=min(mini,num1) 
        maxi=max(maxi,num2)
        operations[3] +=1

    if operations[0] : 
        operations[0]-=1 
        num1,num2 = find_max_min( num + num_list[0], num_list[1:],operations,mini,maxi,string+"+"+str(num_list[0]))
        mini= min(mini,num1)
        maxi= max(maxi,num2)
        operations[0]+=1

    if operations[2] : 
        operations[2] -=1 
        num1,num2= find_max_min(num*num_list[0], num_list[1:], operations,mini,maxi,string+"x"+str(num_list[0]))
        mini=min(mini,num1) 
        maxi=max(maxi,num2)
        operations[2] +=1 

    return mini,maxi

if __name__ =="__main__": 
    # +,-,x,//
    N, num_list, operations = input_data() 
    mini,maxi = find_max_min(num_list[0], num_list[1:], operations, float("inf"),-float("inf"), str(num_list[0])) 
    print(maxi)
    print(mini)