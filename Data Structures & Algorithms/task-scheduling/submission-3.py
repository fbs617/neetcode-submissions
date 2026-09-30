from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        max_heap = []

        freqs = Counter(tasks)

        for freq in freqs.values():
            heapq.heappush(max_heap, -freq)
        
        out = 0
        queue = deque()
        while max_heap or queue:
            if queue and out - queue[0][1] == n + 1:
                curr1 = queue.popleft()
                if curr1[0] < 0:
                    heapq.heappush(max_heap, curr1[0])
            if max_heap:
                curr2 = heapq.heappop(max_heap)
                if curr2 < -1:
                    queue.append([curr2 + 1, out])
            out += 1
        
        return out