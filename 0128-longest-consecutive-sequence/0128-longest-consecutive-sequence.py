class UnionFind:
    def __init__(self,nums):
        self.root = {n:n for n in nums}
        # size = len(nums) if nums else 0
        self.rank = {n:0 for n in nums} 
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


# class UnionFind:
#     def __init__(self):
#         self.parent = {}
#         self.rank = {}

#     def make_set(self, x):
#         self.parent[x] = x
#         self.rank[x] = 0

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             if self.rank[root_x] < self.rank[root_y]:
#                 self.parent[root_x] = root_y
#             elif self.rank[root_x] > self.rank[root_y]:
#                 self.parent[root_y] = root_x
#             else:
#                 self.parent[root_x] = root_y
#                 self.rank[root_y] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        # for num in nums:
            # uf.make_set(num)
        nums = set(nums)
        for num in nums:
            if num + 1 in nums and uf.find(num)!=uf.find(num+1):
                uf.union(num,num+1)
        dic = defaultdict(int)
        for ele in nums:
            dic[uf.find(ele)]+=1
        return max(dic.values()) if dic.values() else 0



        