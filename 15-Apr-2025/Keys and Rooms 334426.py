# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        q = deque()
        q.append(0)
        visited = set()
        
        while q:
            node = q.popleft()
            visited.add(node)
            for key in rooms[node]:
                if key not in visited:
                    q.append(key)
        

        return len(visited) == len(rooms)
        