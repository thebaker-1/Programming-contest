# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque()
        while deck:
            if not q:
                q.append(deck.pop())
                continue
            q.appendleft(q.pop())
            q.appendleft(deck.pop())               
            
        return list(q)


        