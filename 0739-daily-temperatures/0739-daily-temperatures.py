class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer