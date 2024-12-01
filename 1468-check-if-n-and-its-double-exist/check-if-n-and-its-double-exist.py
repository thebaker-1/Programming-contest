class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sets = set(arr)
        dic = defaultdict(int)
        for i in range(len(arr)):
            dic[arr[i]]+=1
            if arr[i]*2 in sets and arr[i]:
                return True
        if dic[0]>1:return True
        return False
        