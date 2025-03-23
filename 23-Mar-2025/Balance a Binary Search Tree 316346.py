# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = []
        def traverse(node):
            if not node:
                return 
            tree.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        tree.sort()
        def bst(l,r):
            if l >r:
                return None
            mid = (l+r)//2
            left = bst(l,mid-1)
            right = bst(mid+1,r)
            node = TreeNode(tree[mid],left,right)
            return node
        return bst(0,len(tree)-1)

        