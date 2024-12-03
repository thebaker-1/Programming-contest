class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        spaceIndex = 0
        change = 0
        s = list(s)
        for i in range(len(s)):
            if spaceIndex < len(spaces) and spaces[spaceIndex]==i:
                spaceIndex+=1
                arr.append(" ")
            arr.append(s[i])
        return "".join(arr)
        