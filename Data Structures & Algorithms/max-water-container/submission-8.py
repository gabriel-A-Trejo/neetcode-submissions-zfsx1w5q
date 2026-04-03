class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            currentHeight = min(heights[l], heights[r])
            area = (r - l) * currentHeight
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result


        