
from sklearn.linear_model import LinearRegression
import pandas 
import numpy as np 
import matplotlib.pyplot as plt 
def random_array2 (size:int) : 
    return np.random.randint(0,100,size=size).reshape(-1,1) 

def random_array (size:int) : 
    return np.random.randint(100,200,size=size).reshape(-1,1)

print(pandas.help())
if __name__ == "__main__":
    X = random_array(100) 
    y = random_array2(100) 

    reg = LinearRegression().fit(X,y) 
    score = reg.score(X,y)
    plt.scatter(y,X)
    plt.plot([0,200], [reg.intercept_, [reg.coef_+reg.intercept_]],'r')
    plt.show()
    print(score)
    print(reg.coef_)
    print(reg.intercept_)