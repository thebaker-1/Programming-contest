# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def rec(node):
            if node:
                if node.val > val:
                    if not node.left:
                        return node
                    return rec(node.left)
                else:
                    if not node.right:
                        return node
                    return rec(node.right)
        node = rec(root)
        if node.val > val:
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)
        return root
                
        