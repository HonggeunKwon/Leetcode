class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, current in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current:
                last = stack.pop()
                answer[last] = idx - last
            
            stack.append(idx)
        return answer