class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
            cars = {}
            for i in range(len(position)):
                cars[position[i]] = speed[i]

            position.sort()

            stack = []
            for i in range(len(position)):
                pos, speed = position[i], cars[position[i]]

                time = (target - pos) / speed

                while stack and time >= stack[-1]:
                    stack.pop()
                
                stack.append(time)
            return len(stack)
            
