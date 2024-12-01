class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sets = set(arr)
        for i in range(len(arr)):
                if arr[i]*2 in sets and arr[i]:
                    return True
        dic = Counter(arr)
        if dic[0]>1:return True
        return False
        