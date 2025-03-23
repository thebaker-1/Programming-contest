# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l,r):
            if l > r:
                return None
            mid = (l+r)//2
            n = TreeNode(nums[mid])
            n.left = bst(l,mid-1)
            n.right = bst(mid+1,r)
            return n

        return bst(0,len(nums)-1)
        