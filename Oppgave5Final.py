#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:07:26 2025

@author: thomas
"""

import math

def omkrets(a,b):
    return math.sqrt(a**2+b**2)+b+(a*math.pi)
print("Omkretsen av figuren er", omkrets(2,5))

def areal(a,b):
    sirkelAreal = (math.pi*a**2)/2
    trekantAreal = (a*b)/2
    return sirkelAreal + trekantAreal

print("Arealet av figuren er", areal(2,5))