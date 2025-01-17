#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:48:12 2025

@author: thomas
"""

import math

antall_elever = int(input("Skriv inn antall elever: "))
andel = 0.25
antall_pizza = antall_elever*andel
print(f"Pizzaer som må kjøpes til",antall_elever,"elever er",math.ceil(antall_pizza),"stk")