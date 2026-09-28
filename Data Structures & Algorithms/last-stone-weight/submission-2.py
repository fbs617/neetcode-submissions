import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [(-1 * stone) for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heavy1 = -1 * heapq.heappop(heap)
            heavy2 = -1 * heapq.heappop(heap)
            if heavy1 < heavy2:
                heavy2 -= heavy1
                heapq.heappush(heap, -1 * heavy2)
            elif heavy2 < heavy1:
                heavy1 -= heavy2
                heapq.heappush(heap, -1 * heavy1)
        if heap:
            return -1 * heap[0]
        return 0

            