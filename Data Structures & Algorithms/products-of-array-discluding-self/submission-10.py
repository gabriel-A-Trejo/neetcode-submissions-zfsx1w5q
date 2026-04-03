class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        update_array = []
        previous = 1
        for i in range(len(nums)):
            update_array.append(previous)
            previous *= nums[i]
        
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            update_array[j] *= suffix
            suffix *= nums[j]

        return update_array

