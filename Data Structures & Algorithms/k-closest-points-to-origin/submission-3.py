import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            curr = points[i]
            euclid = (curr[0] * curr[0]) + (curr[1] * curr[1])
            heapq.heappush(heap, (euclid, i))
        out = []
        for i in range(k):
            out.append(points[heapq.heappop(heap)[1]])
        return out
            


