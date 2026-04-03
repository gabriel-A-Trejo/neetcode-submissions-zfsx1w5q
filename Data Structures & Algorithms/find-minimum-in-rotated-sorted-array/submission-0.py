class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Edge case when l < r then return the min of result
        #Edge when is empty return 


        #When l > r then we do the binary search from m = (l + R) // 2
        #if when nums l > r then l = m + 1 else r = m - 1 we update l to return the min
        #then return the result

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        
