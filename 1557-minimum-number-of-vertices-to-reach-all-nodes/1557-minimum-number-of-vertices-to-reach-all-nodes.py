class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        set_graph = set()
        res = []
        for e,v in edges:
            set_graph.add(v)
        for i in range(n):
            if i not in set_graph:
                res.append(i)
        return res
