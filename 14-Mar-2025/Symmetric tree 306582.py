# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(n1,n2):
            if not n1:
                if n2:
                    return False
                return True
            if not n2:
                if n1:
                    return False
                return True
            if n1.val != n2.val:
                return False
            a = rec(n1.left,n2.right)
            b = rec(n1.right,n2.left)
            return a and b
        return rec(root,root)

        