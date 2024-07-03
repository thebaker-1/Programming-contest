"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        l = defaultdict(list)
        self.max_level = 0
        def dfs(node,level):
            if not node:
                return
            self.max_level = max(self.max_level,level+1)
            l[level].append(node.val)
            for child in node.children:
                dfs(child,level+1)
        dfs(root,0)
        return self.max_level
            