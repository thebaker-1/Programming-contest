class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        index = 0
        for space in spaces:
            arr.append(s[index:space])
            index=space
        arr.append(s[index:])
        return " ".join(arr)
        