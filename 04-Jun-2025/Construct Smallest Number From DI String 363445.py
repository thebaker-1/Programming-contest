# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        combinations = [str(i) for i in range(1,10)]
        for i in pattern:
            newcombinations = []
            if i == "I":
                for cur in combinations:
                    for i in range(int(cur[-1])+1,9+1):
                        if str(i) not in cur:
                            newcombinations.append(cur + str(i))
            else:
                for cur in combinations:
                    for i in range(1,int(cur[-1])):
                        if str(i) not in cur:
                            newcombinations.append(cur + str(i))
            combinations = newcombinations

        combinations.sort()
        return combinations[0]
