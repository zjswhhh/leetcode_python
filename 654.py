# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)

        l_nums = nums[:max_index]
        r_nums = nums[max_index + 1:]

        node = TreeNode(max_val)
        node.left = self.constructMaximumBinaryTree(l_nums)
        node.right = self.constructMaximumBinaryTree(r_nums)