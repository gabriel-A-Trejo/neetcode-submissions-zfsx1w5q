class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Lets set up a binary search 
        l, r = 0, len(nums) - 1
        #lets get current result by setting at the begining 
        result = nums[0]

        #lets create the while loop:
        while l <= r:
            #Check to see if left is indeed less then right which we can able use to the min to set it up
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = l + (r - l) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result
            
        