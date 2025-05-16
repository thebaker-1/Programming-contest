# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        stobit = defaultdict(int)
        stobit["a"] = int("1",2)
        stobit["e"] = int("10",2)
        stobit["i"] = int("100",2)
        stobit["o"] = int("1000",2)
        stobit["u"] = int("10000",2)
    
        initial = {0:-1}
        prefix = [0]
        maxlen = 0
        for i,letter in enumerate(s):
            num = stobit[letter]
            new = num ^ prefix[-1]
            prefix.append(new)
            if new not in initial:
                initial[new] = i
            else:
                maxlen = max(maxlen,i - initial[new])
        return maxlen
            




        