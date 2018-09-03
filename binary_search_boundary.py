#!/usr/bin/python
# -*- coding: UTF-8 -*-

# To discuss all possible boundary situation when utilizing binary search

#    :type A: List[int] target: int
#    :rtype: int

# 1. Index where target occurs for the first time
def FirstIndex(A, target):
    left, right = 0, len(A) - 1

    while left < right :
        mid = left + (right - left) / 2
        if A[mid] < target:
        	left = mid + 1
        else:
        	right = mid

    if A[left] == target:
    	return left
    else:
    	return -1


# 2. Index where target occurs for the last time 
def LastIndex(A, target):
	left, right = 0, len(A) - 1

	while left < right :
		mid = left + (right - left + 1) / 2
		if A[mid] > target:
			right = mid - 1
		else:
			left = mid

	if A[left] == target:
		return left
	else:
		return -1


# When it comes to monotonically decreasing array, just switch the '<' and '>'

# test
arr = [1, 2, 3, 3, 3, 3, 5]
print FirstIndex(arr, 3), LastIndex(arr, 3)






