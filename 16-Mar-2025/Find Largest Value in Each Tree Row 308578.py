# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            len_row = len(q)
            maxi = -float("inf")
            for i in range(len_row):
                node = q.popleft()
                maxi = max(maxi,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            res.append(maxi)
        return res
            
        