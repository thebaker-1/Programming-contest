# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        q = deque([('',0,0)])
        visited ={('',0,0)}
        step = -1

        while q:
            step += 1

            for _ in range(len(q)):
                word,i,j = q.popleft()
                if word == key:
                    return step
                visited.add((word,i,j))
                if ring[i] == key[j]:
                    new_word = word+ring[i]
                    if (new_word,i,j+1) not in visited:
                        q.append((new_word,i,j+1))
                        visited.add((new_word,i,j+1))
                else:
                    go_back = (word,(i-1)% len(ring),j)
                    go_front = (word,(i+1)% len(ring),j)
                    if go_front not in visited:
                        q.append(go_front)
                        visited.add(go_front)
                    if go_back not in visited:
                        q.append(go_back)
                        visited.add(go_back)
        return -1


        