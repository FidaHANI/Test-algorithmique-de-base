# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:47:25 2016

@author: fida
"""
# Exercice 3

import sys
import inspect

class Node:
    def __init__(self, val):
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
    
  def __init__(self, node):
      self.root = node
      
  def add(self, val):
      if(self.root == None):
          self.root = Node(val)
      else:
          self.insert(val, self.root)
          
  def insert(self, val, node):
        if(val <= node.value):
            if(node.left is not None):
                self.insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right is not None):
                self.insert(val, node.right)
            else:
                node.right = Node(val)
                
  def run(self, val):
       if(self.root is not None):
           return self.find(val, self.root)
       else:
           return None
            
  def find(self, val, node):
        if(val == node.value):
            return True 
        elif(val < node.value and node.left is not None):
            return self.find(val, node.left)
        elif(val > node.value and node.right is not None):
            return self.find(val, node.right)
        else:
            return False
  def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
      
### Testing an example
if __name__ == '__main__':
    tree = Tree(Node(1))
    li = [7, 5, 3,2]
    for s in li:
        tree.add(s)
    print tree.run(2)
    print tree.run(10)
    print tree.get_classes()












































































