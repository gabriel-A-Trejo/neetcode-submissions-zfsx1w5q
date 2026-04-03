class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #first we need to have a container
        container = 0 
        #Traverse using two pointers
        l = 0 
        r = len(heights) - 1

        while l < r:
            area = min(heights[r], heights[l]) * (r - l)
            container = max(container, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return container



