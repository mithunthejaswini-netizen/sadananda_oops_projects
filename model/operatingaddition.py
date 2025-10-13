# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 21:29:20 2025

@author: meetm
"""

class Sadananda:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __iadd__(self,spirit):
        
        self.x+=spirit.x
        self.y+=spirit.y
        
        return self

    def __str__(self):
        return f'{self.x=} {self.y=}'
        
a = Sadananda(32, 85)
b = Sadananda(23, 33)
c = Sadananda(22, 31)

k = [b, c]

for obj in k:
    a+= obj
    
print(a)
