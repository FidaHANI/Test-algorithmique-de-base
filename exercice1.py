#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:53:32 2016

@author: fida
"""

# Exercice 1 

import sys
import inspect

class Sum : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       s=0
       for i in xrange(self.n+1):
           if (i%3)==0 or (i%5)==0:
               s+=i
       return s
   
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)

# Testing an example
if __name__ == '__main__':        
    sum = Sum(20)
    print sum.run()
    print sum.get_classes()
    
    
 