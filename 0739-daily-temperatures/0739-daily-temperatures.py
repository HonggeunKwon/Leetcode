class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        s = []
        
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                idx = s.pop()
                answer[idx] = i - idx
            s.append(i)
        
        return answer
        