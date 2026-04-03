from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # stores tuples of (height, index)

        for currentIndex, currentHeight in enumerate(heights):
            start = currentIndex
            while stack and currentHeight < stack[-1][0]:
                prevHeight, prevIndex = stack.pop()
                width = currentIndex - prevIndex
                area = prevHeight * width
                maxArea = max(maxArea, area)
                start = prevIndex
            stack.append((currentHeight, start))
        
        while stack:
            prevHeight, prevIndex = stack.pop()
            width = len(heights) - prevIndex
            area = prevHeight * width
            maxArea = max(maxArea, area)
        
        return maxArea