# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        def dfs(key):
            for new_key in rooms[key]:
                if new_key not in visited:
                    visited.add(new_key)
                    dfs(new_key)
        dfs(0)

        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True
        