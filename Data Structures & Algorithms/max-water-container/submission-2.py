class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            Plan:
            We need to calculate the area  based container we able to use two pointer
            THus we can able find the min of left and right then can we able to find the min from it 
            We can use the area by finding min height and calcualte based on r - l
            Next step we conitnue until we find the max
        """

        maxsum = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l],heights[r]) * (r - l)
            maxsum = max(maxsum, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxsum
        