# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:47:29 2016

@author: fida
"""
# Exercice 1 

import sys
import inspect

## Example 1: Using recursion

class Recursion : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       return self.fibR(self.n+2)-1 #
       
   def fibR(self,index):
       if index==0: 
           return 0
       elif index==1:
           return 1
       return self.fibR(index-1)+self.fibR(index-2)
       
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)  

# Testing an n value
if __name__ == '__main__':
    recursion = Recursion(6)
    print recursion.run()
    print recursion.get_classes()

## Example 2: Using looping technique

class Looping : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       a,b = 1,1
       for i in range(self.n+1):
           a,b = b,a+b
       return a-1
     
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)

# Testing an n value
if __name__ == '__main__':
    looping = Looping(6)
    print looping.run()
    print looping.get_classes()      
       
## Example 3: Using Functional Expression
       
from math import sqrt

class Formula : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       index=self.n+2
       return (((1+sqrt(5))**index-(1-sqrt(5))**index)/(2**index*sqrt(5)))-1
   
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
   
# Testing an n value
if __name__ == '__main__':
    formula = Formula(6)
    print formula.run()
    print formula.get_classes()        
       
"""
Firstly, I should note that in the previous algorithms, I used the result saying that 
the sum of the first n Fibonacci numbers is the (n + 2)nd Fibonacci number minus 1.

The first implemented method is based on a recirsive process. in this case, some elements are calculated 
more twice, which is redundant. Hence, the calculation time is increased vainly.

The second example exhibts a looping technique which consumes less time than the recursive method.

Finally, the third algorithm needs only the calculation of a mathematical formula for the Fibonacci term(n+2) minus 1. 
Clearly, This one is pretty easy to implement and is very fast to compute compared to the methods above.         

"""
      
       
       
       
       
       
       
       
       
       
