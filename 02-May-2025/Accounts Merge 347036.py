# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, size,accounts):

        self.parent = defaultdict(str)
        for account in accounts:
            for i in range(1,len(account)):
                self.parent[account[i]] = account[i]
        self.size = {self.parent[i]:1 for i in self.parent.values()}

    def find(self, x):
        # Write your code here
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

		
    def union(self, x, y):
        # Write your code here
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.size[parx] >= self.size[pary]:
                self.parent[pary] = parx
                self.size[parx] += self.size[pary]
            else:
                self.parent[parx] = pary
                self.size[pary]  += self.size[parx]
                

    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts),accounts)
        email_name = defaultdict(str)
        for account in accounts:
            for i in range(1,len(account)):
                email_name[account[i]] = account[0]
                uf.union(account[1],account[i])
        
        new_accounts = defaultdict(list)
        for i,val in uf.parent.items():
            new_accounts[uf.find(i)].append(i)

        res = []
        for i,val in new_accounts.items():
            half_res = []
            for email in val:
                half_res.append(email)
            half_res.sort()
            res.append([email_name[i]] + half_res)
        return res






        