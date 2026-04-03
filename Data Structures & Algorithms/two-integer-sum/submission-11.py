class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We need to traverse the array with the current index
        #Create a hashmap data structure
        hashmap = {}
        for i in range(len(nums)):
            #we will see if the complement has it in the DSA
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            #add the index as the value and value as in the index in nums
            hashmap[nums[i]] = i
        