# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur == p:
                return p
            elif cur == q:
                return q
            elif (cur.val > p.val and cur.val < q.val) or (cur.val < p.val and cur.val > q.val):
                return cur
            elif cur.val > p.val and cur.val > q.val:
                return self.lowestCommonAncestor(cur.left,p,q)
            else:
                return self.lowestCommonAncestor(cur.right,p,q)
        



        