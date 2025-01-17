#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:15:30 2025

@author: thomas
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2-5
x = np.linspace(-10,10,200)
y = f(x)

plt.plot(x,y)
plt.show()