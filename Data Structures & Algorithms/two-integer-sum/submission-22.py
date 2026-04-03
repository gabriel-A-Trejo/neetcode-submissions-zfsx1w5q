class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Data structure: a dictionary where we key is the value and value is index of the array
        #we will traverse the lenght of the nums and find if the dictionary has right calcuation wehter or not is already in the dictureion else we will return [-1, -1]

        length_nums = len(nums)
        viewed = {}

        for index in range(length_nums):
            complement = target - nums[index]
            if complement in viewed:
                return [viewed[complement], index]
            viewed[nums[index]] = index
        

        
        