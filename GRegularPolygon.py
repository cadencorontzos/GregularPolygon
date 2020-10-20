#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:37:43 2019

@author: cadecorontzos
"""
from pgl import GPolygon, GWindow
from math import cos,sin,tan,radians, pi, degrees

class GRegularPolygon(GPolygon):
    
    def __init__(self,nSides,radius):
        
        """
        Initializes the Regular Polygon of the given perameters. The reference point is the center of the shape.
        """
        GPolygon.__init__(self)
        self.nSides=nSides
        self.radius=radius
    
        theta=radians(360/self.nSides)
        interiorTheta=radians(((self.nSides-2)*180)/self.nSides)
        sideLen=2*self.radius*sin(theta/2)
        self.addVertex(-sideLen/2,self.radius*cos(theta/2))
        
        newTheta=0
        for i in range(self.nSides-1):
            self.addPolarEdge(sideLen,degrees(newTheta))
            newTheta+=(pi-interiorTheta)
            
    def __str__(self):
        
        return "GRegularPolygon(" +str(self.nSides)+" sides, " + str(self.radius) + " radius)"
    
    def getType(self):
        
        """
        Returns the type of this object.
        """
        
        return "GRegularPolygon"
            
    def getNSides(self):
        """
        Returns the number of sides of the polygon.
        """
        return self.nSides
    
    def getRadius(self):
        """
        Returns the radius of the polygon.
        """
        return self.radius
            
def tester():
    
    sideLen=100
    print("How many sides do you want your regular polygon to have? Enter a positive integer.")
    iPut = int(input())
    gw=GWindow(sideLen*3,sideLen*3)
    gr=GRegularPolygon(iPut,30)
    gw.add(gr,gw.getWidth()/2,gw.getHeight()/2)

    
#Startup Code
    
if __name__=="__main__":
    tester()
