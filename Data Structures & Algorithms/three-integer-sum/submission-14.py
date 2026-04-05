class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, value in enumerate(nums):
            if value > 0:
                break
            if index > 0 and value == nums[index - 1]:
                continue
            
            l, r = index + 1, len(nums) - 1

            while l < r:
                currentSum = value + nums[l] + nums[r]

                if currentSum == 0:
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                
                elif currentSum > 0:
                    r -= 1
                else:
                    l += 1
        return result

        