# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	x = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return x,y

print(quadratic(2, 3, 1)) 
print(quadratic(1, 3, -4))