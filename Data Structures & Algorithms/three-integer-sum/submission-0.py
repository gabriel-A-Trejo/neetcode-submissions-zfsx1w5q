class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to store an array
        result = []

        #we need to sort the array
        nums.sort()

        #We need to create an offset 
        for offset in range(len(nums)):
            #Check to avoid duplicates
            if offset > 0 and nums[offset] == nums[offset - 1]:
                continue
            l = offset + 1
            r = len(nums) - 1
            while l < r: 
                currentSum = nums[offset] + nums[l] + nums[r]
                if currentSum == 0:
                    result.append([nums[offset], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    #check for duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif currentSum > 0:
                    r -= 1
                else:
                    l += 1
        return result
                    

        