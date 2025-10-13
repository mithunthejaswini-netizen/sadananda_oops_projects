# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 21:19:33 2025

@author: meetm
"""

class Sadananda:
    
    def __init__(self,name):
        self.name = name
        
    def __eq__(self, other):
        return self.name==other.name
    
    def __hash__(self):
        return hash(self.name)
        
        
s = set()

s1 = Sadananda('sadananda')
s2 = Sadananda('maharaj')
s3 = Sadananda('muthya')
s4 = Sadananda('maharaj')

s.add(s1)
s.add(s2)
s.add(s3)
s.add(s4)

print(s)