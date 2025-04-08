# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        valid_letter = set()

        for i,val in enumerate(equations):
            left,right = val
            graph[left].append((right,values[i]))
            graph[right].append((left,1/values[i]))
            valid_letter.add(left)
            valid_letter.add(right)
        print(graph)

    
        def dfs(source,destination):
            nonlocal flag

            if destination == source:
                if source in valid_letter:
                    flag = True
                    return 1
                return -1

            for letter in graph[source]:
                nbr , val = letter
                if nbr not in visited:
                    visited.add(nbr)
                    find_ans = dfs(nbr,destination)
                    if find_ans and flag:
                        return find_ans * val
            return -1


        visited=set()
        ans = []
        for left,right in queries:
            visited.add(left)
            flag = False
            x = dfs(left,right)
            if x < 0:
                ans.append(-1)
            else:
                ans.append(x)
            visited = set()
        return ans

        