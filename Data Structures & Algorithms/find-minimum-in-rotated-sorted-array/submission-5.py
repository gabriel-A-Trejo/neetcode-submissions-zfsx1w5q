class Solution:
    def findMin(self, nums: List[int]) -> int:

        #We do the same pattern of the binary search 
        #We can start by using result to first index

        #Next step is to able figure out on is having the same binary search pattern

        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = (l + r) // 2
            #we can find the mid when find mid level based on the mid
            
            result = min(result, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result 
        




        