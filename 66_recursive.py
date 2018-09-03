#!/usr/bin/python
# -*- coding: UTF-8 -*-

def plusOne(digits):

    """
    :type digits: List[int]
    :rtype: List[int]
    """

    if digits == []:
        return digits
    if digits == [9]:
        return [1, 0]
    if digits[-1] < 9:
        return digits[:-1] + [digits[-1]+1]
    else:
        return plusOne(digits[:-1]) + [0]



#test

a = [1, 3, 9]
print plusOne(a)
