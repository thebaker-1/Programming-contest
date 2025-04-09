# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a , b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(dislike):
            q = deque()
            q.append(dislike)
            color = defaultdict(int)
            color[dislike] = 1
            flag = True
            while q:
                val = q.popleft()
                visited.add(val)
                for i in graph[val]:
                    if color[i] == 0:
                        q.append(i)
                        visited.add(i)
                        color[i] = -1*color[val]
                    else:
                        if color[i] == color[val]:
                            flag = False
                            break
                if not flag:
                    return False
            return flag

        visited = set()
        for i in range(1,n+1):
            if i not in visited:
                res = dfs(i)
                if not res:
                    return False
        return True





