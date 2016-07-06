#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Please input a:')
a = input()
print('Please input b:')
b = input()
print('Please input c:')
c = input()

import math

def quadratic(a,b,c):
	x = (-b + math.sqrt(b*b-4*a*c))/(2*a)
	y = (-b - math.sqrt(b*b-4*a*c))/(2*a)
	return x,y

print (quadratic(a,b,c))