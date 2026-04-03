class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []


        for key, value in enumerate(nums):
            if value > 0:
                break
            if key > 0 and nums[key] == nums[key - 1]:
                continue
            l, r = key + 1, len(nums) - 1
            while l < r:
                currentSum = value + nums[l] + nums[r]
                if currentSum  == 0:
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    r -= 1
        return result