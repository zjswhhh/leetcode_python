#!/usr/bin/python
# -*- coding: UTF-8 -*-


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def test(root):
    if not root:
        return []

    ans = []
    queue = []
    queue.append(root)
    row = []
    temp = []
    while(len(queue)>0):
        node = queue.pop(0)
        row.append(node.val)
        if node.left:
            temp.append(node.left)
        if node.right:
            temp.append(node.right)
        if len(queue) == 0:
                queue = temp
                temp = []
                ans.append(row)
                row = []

    return ans


