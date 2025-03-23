# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q  = deque()
        q.append(root)
        tf = True
        tree = deque()
        while q:
            tf = not tf
            length = len(q)
            level = []
            for _ in range(length):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if tf:
                for i in range(len(level)//2):
                    level[i].val, level[-(i+1)].val =  level[-(i+1)].val,level[i].val
        return root