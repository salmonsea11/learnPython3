#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 冒泡排序

def bubble_sort(lists):
	count = len(lists)
	for i in range(0,count):
		for j in range(i+1,count)
			if lists[i] > lists[j]:
				temp = lists[j]
				lists[j] = lists[i]
				lists[i] = temp
	return lists