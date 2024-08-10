class UnionFind:
    def __init__(self,nums):
        self.root = {n:n for n in nums}
        # self.rank = [1] * size
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            # elif self.rank[rootX] < self.rank[rootY]:
            #     self.root[rootX] = rootY
            # else:
            #     self.root[rootY] = rootX
            #     self.rank[rootX] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        nums = set(nums)
        for num in nums:
            if num + 1 in nums and uf.find(num)!=uf.find(num+1):
                uf.union(num,num+1)
        dic = defaultdict(int)
        for ele in nums:
            dic[uf.find(ele)]+=1
        return max(dic.values()) if dic.values() else 0



        