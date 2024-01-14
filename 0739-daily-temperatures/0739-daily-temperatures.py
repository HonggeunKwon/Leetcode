class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures);
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pre_idx = stack.pop()
                answer[pre_idx] = i - pre_idx
            stack.append(i)
        
        return answer
        