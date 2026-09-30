from heapq import heapify_max, heappop_max, heappush_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            first_largest = heappop_max(stones)
            second_largest = heappop_max(stones)
            if first_largest != second_largest:
                heappush_max(stones, abs(second_largest-first_largest))
        return heappop_max(stones) if stones else 0


        