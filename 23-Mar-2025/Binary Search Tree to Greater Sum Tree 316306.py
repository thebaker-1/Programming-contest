# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def traversal(node):
            nonlocal total
            if not node:
                return 0
            traversal(node.right)
            node.val += total
            total = node.val
            traversal(node.left)
        traversal(root)
        return root

