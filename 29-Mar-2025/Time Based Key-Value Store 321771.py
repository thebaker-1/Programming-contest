# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        res = []
        def valid(i):
            if self.dic[key][i][0] > timestamp:
                return False
            return True
        l = 0
        r = len(self.dic[key]) - 1
        while l <= r:
            mid = (l + r)//2
            if valid(mid):
                l = mid + 1
            else:
                r = mid - 1
        if self.dic[key][0][0] > timestamp:
            return ""
        return self.dic[key][r][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)