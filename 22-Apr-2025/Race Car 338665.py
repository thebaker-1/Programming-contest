# Problem: Race Car - https://leetcode.com/problems/race-car/description/

class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0,1))
        step = -1
        visited = set()
        while q:
            step += 1
            length = len(q)
            for _ in range(length):
                pos,speed = q.popleft()
                if pos == target:
                    return step
                if (pos, speed) in visited:
                    continue
                visited.add((pos,speed))
                pos1 = pos + speed
                if 0 <= pos1 <= target * 2:
                    q.append((pos1,speed*2))
                if speed < 0:
                    speed2 = 1
                else:
                    speed2 = -1
                q.append((pos,speed2))
        return -1