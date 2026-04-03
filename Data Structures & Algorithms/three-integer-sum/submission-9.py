class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        #Create a loop since we need three pointers one will be in the starting point

        for index, value in enumerate(nums):
            if value > 0:
                break
            
            if index > 0 and value == nums[index - 1]:
                continue
            
            #Same pattern as before 

            l, r = index + 1, len(nums) - 1

            while l < r:
                currentSum = value + nums[l] + nums[r]
                if currentSum == 0:
                    result.append([value, nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    r -= 1
        return result