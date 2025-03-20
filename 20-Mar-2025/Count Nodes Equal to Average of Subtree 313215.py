# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def rec(node):
            nonlocal res
            if not node:
                return [0,0]
            suml,countl = rec(node.left)
            sumr,countr = rec(node.right)
            sumn = suml + sumr + node.val
            countn = countl + countr + 1
            if sumn//countn == node.val:
                res += 1
            return [sumn,countn]
        rec(root)
        return res



