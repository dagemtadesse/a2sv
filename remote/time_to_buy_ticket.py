class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        timeTaken = 0

        que = tickets[::]
        index = 0

        while que[k] != 0:
            if que[index] > 0:
                que[index] -= 1
                timeTaken += 1
            index = (index + 1) % len(tickets)
        return timeTaken
            
