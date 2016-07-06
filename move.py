#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用递归函数移动汉诺塔：
def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
		return
	move(n-1,a,c,b)
	print(a,'-->',c)
	move(n-1,b,a,c)

move(3,'A','B','C')