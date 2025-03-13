# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preorder(node):
            temp = []
            if not node:
                return temp
            temp.append(node.val)
            temp.extend(preorder(node.left))
            temp.extend(preorder(node.right))

            return temp
        
        return preorder(root)



        