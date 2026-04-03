class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lengthTemperature = len(temperatures)
        stack = []

        result = [0] * lengthTemperature

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((t, i))
        
        return result