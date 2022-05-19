fibo = [0,1]
n = int(input()) 
if n == 1:
    print(fibo[1])
elif n == 0 :
    print(fibo[0]) 
else:
    n = n-1
    fibo3= 0
    for _ in range(n%(15*(10**5))): # 피사노 주기 10^n까지의 나머지를 구할때 피보나치 수열은 15*10^n-1번째까지의 숫자가 반복된다. 
        fibo.append(fibo[-1]+fibo[-2])
        
    print(fibo[-1]%1000000)