class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]: # 가장 마지막에 들어온 것 보다 더 높으면,
                top = stack.pop()
                
                if len(stack) == 0:
                    break
               
                distance = i - stack[-1] - 1
                water = min(height[stack[-1]], height[i]) - height[top]
                
                volume += distance * water
                
            stack.append(i)
            
        return volume