class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            heapq.heappush(gifts,-floor(math.sqrt(-heapq.heappop(gifts))))
        return -sum(gifts)
        