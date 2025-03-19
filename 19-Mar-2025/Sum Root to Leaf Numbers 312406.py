# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node,string):
            if not node:
                self.res += int(string)
                return 
            string += str(node.val) 
            if node.left and node.right:
                dfs(node.left,string)
                dfs(node.right,string)
            elif node.left:
                dfs(node.left,string)
            else:
                dfs(node.right,string)
        dfs(root,str())
        return self.res



        