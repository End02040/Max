# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:14:02 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
    
    
    
   x=x+j 
 r = randrang(0,16)   
    
    
for i in range(10):
    Max.setBlock(x,y,z,35,r)
    z=z+1

while True:
    hit = Max.events.pollBlockHits()
    if len(hits)>0:
        h= hits[0]

    block = Max.getBlpckWithData(h.pos)
    data = block.data
    if data==r:
        Max.postToChat("Good")
        Max.setBlock(h.pos,57)
    elif data>r:
        Max.postToChat("LOL")
 elif data<r:
        Max.postToChat("LOL")
