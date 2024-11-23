class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lettersbool = [False]*26
        stodict = defaultdict(int)
        for i in s:
            stodict[i]+=1
        res = []
        for val in order:
            if val in stodict:
                res.extend([val]*stodict[val])
                lettersbool[ord(val)-ord("a")]= True
        for val in s:
            if not lettersbool[ord(val)-ord("a")]:
                res.append(val)
        return "".join(res)
