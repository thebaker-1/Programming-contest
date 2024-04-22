class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        sum = 0
        curr = 0
        for k in range(len(s)):
            if k== 0 or s[k] == s[k-1]:
                curr +=1
            else:
                sum += min(prev,curr)
                prev=curr
                curr = 1
            if k == len(s)-1:
                sum += min (prev,curr)
        return sum

        