#TODO: test case -> for
#TODO: make queue 
    #TODO: push, pop 

from typing import Optional
import random

class Q (): 
    __stack1: list
    __stack2: list
    size: int
    def __init__ (self, size=None):
        self.__stack1 = []
        self.__stack2 = []
        if size : 
            self.size = size

    def push(self,item:any) -> None : 
        self.__stack1.append(item)

    def pop(self,)->all:
        if not (self.__stack1 or self.__stack2): 
            print("queue is empty!")
            return 

        elif not self.__stack2:
            while self.__stack1 :
                item = self.__stack1.pop()
                self.__stack2.append(item)
        return self.__stack2.pop()

class Q2(Q):
    __stack3 = []

def random_push(q:Q, size:int,) -> None:
    print("push: ", end='')
    for _ in range(size):
        item = random.randint(0,100)
        print(item," ", end='')
        q.push(item)
    print("")

def random_pop(q:Q, size:int) -> all: 
    print("pop: ", end='')
    for _ in range(size):
        print(que.pop()," ", end='')
    print("")

if __name__=="__main__":
    que = Q()
    
    random_push(que, 10)
    random_pop(que,5)
    random_push(que,10)
    random_pop(que,15)
    