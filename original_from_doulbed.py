class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = {}
        original = []

        changed.sort()

        for i in changed:
            
            if i in count:
                count[i] += 1
                if count[i] == 0: del count[i]
                original.append(i // 2)
            else:
                if (i * 2) in count:
                    count[i * 2] += -1
                else: count[i * 2] = -1            

        return original if len(original) == (len(changed) / 2) and (not bool(count)) else []