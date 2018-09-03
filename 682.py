#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """

    stack = []
    for op in ops:
        if op == '+' :
            stack.append(stack[-1]+stack[-2])
        elif op == 'D' :
        	stack.append(2*stack[-1])
        elif op == 'C' :
       		stack.pop()
        else: 
       		stack.append(int(op))

    return sum(stack)




ops = ["5","2","C","D","+"]
print(calPoints(ops))
