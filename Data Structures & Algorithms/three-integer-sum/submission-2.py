class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = value + nums[left] + nums[right]
                print(three_sum)
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    print([value, nums[left], nums[right] ])
                    res.append([value, nums[left], nums[right] ])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                    
        return res
                    

