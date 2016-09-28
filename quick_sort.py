#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 快速排序

def quick_sort(lists,left,right):
	if left >= right:
		return lists
	key = lists[left]
	low = left
	hight = right
	while left < right:
		while left < right and lists[right] >= key:
			right -=1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left +=1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists,low,left -1)
	quick_sort(lists,left +1,high)
	return lists