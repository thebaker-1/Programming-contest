# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def rec(node,big,small):
            if not node:
                return 0 
            big = max(big,node.val)
            small = min(small,node.val)
            res = abs(big-small)
            x = max(rec(node.left,big,small),abs(big - small))
            y = max(rec(node.right,big,small), abs(big - small))
            return max(x,y)
        return rec(root,-float("inf"),float("inf"))
            



        