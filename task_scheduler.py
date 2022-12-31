from typing import List
from queue import PriorityQueue

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        pq = PriorityQueue()
        length = 0

        for task in tasks:
            if task in count:
                count[task] += 1
            else: count[task] = 1
        
        for (key, value) in count.items():
            pq.put((-value, key))

        print(pq.queue)
        # print(sorted(count.items(), key=lambda item: item[1]))
        while not pq.empty():
            removed = []
            

            for i in range(n + 1):
                if not pq.empty():
                    (count, key) = pq.get()
                    length += 1
                    # print(key, end=" ")
                    if count < -1:
                        removed.append((count, key))
                elif removed:
                    # print('_', end=" ")
                    length += 1
            # print()
            for item in removed:
                (count, key) = item
                if(count < -1):
                    pq.put((count + 1, key))

            removed = []

        return length
                
        
        

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

# [B, C, A]
# A B C A