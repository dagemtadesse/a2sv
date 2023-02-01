class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = [(temperatures[0], 0)]
        index = 1

        while len(stack) > 0:
            current = temperatures[index]
            prev, prevIndex = stack.pop()
            
            while True:
                if prev < current:
                    answer[prevIndex] = index - prevIndex
                    if stack:
                        prev, prevIndex = stack.pop()
                    else:
                        break
                else:
                    stack.append((prev, prevIndex))
                    break

            if index < len(temperatures) - 1:
                stack.append((current, index))
                index += 1
            elif stack:
                stack.pop()
        return answer