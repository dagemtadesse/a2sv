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
                    print(key, end=" ")
                    if count < -1:
                        removed.append((count, key))
                elif removed:
                    print('_', end=" ")
                    length += 1
            print()
            # print(pq.queue,"->", removed)
            for item in removed:
                (count, key) = item
                if(count < -1):
                    pq.put((count + 1, key))

            removed = []

            # if len(queue) >= n + 1:
            #     queue.pop(0)

            # selected = None
            # for task in count.keys():
            #     size = count.get(selected) if count.get(selected) != None else 0
            #     if not task in queue and size < count[task]:
            #         selected = task

            # queue.append(selected)
            # length += 1

            # if not selected is None:
            #     count[selected] -= 1
            #     if count[selected] <= 0:
            #         del count[selected]
        
            # print(selected, end=" ")
        return length
                
        
        

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

# [B, C, A]
# A B C A