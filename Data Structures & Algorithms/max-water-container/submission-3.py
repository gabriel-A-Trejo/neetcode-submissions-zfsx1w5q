class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: 
            return 0
        result = 0
        #First we need to find width which is r - l
        #NEext is times by the min(width that can contian the water)
        l, r = 0, len(heights) - 1
        #Follow the two pointer pattern
        while l < r:
            #find the width
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            result = max(result, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result




        #Result but result to max value of them all

