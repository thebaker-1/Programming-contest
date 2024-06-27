# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        self.res = 0 
        def check(node, mini , maxi):
            if not node:
                return
            self.res = max(self.res, abs(node.val- mini), abs(node.val-maxi))
            if node:
                check(node.left, min(mini,node.val),max(maxi,node.val))
                check(node.right,min(mini,node.val),max(maxi,node.val))
        check(root,root.val,root.val)
        return self.res


        





