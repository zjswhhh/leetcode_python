#!/usr/bin/python
# -*- coding: UTF-8 -*-

def plusOne(digits):

    """
    :type digits: List[int]
    :rtype: List[int]
    """

    l = list(str(int(''.join(map(str, digits)))+1))
    return [int(i) for i in l]


#test

a = [1, 3, 9]
print plusOne(a)
