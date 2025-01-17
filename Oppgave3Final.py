#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:57:28 2025

@author: thomas
"""

import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))
v_rad = v_grad*np.pi/180

print(f"{v_grad} grader er lik {v_rad} radianer")