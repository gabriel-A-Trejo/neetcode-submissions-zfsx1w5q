class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We are going to have an hashmpa to keep track based on the index
        #Value : index
        hashmap = {}


        #Create a for loop
        for i in range(len(nums)):
        #What can determin is based on a complement when target - current
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
        #then we will check to see current complement is laready in there if it is
        #then return [hashmap[complement], i]

        # add the current value based on the index -> value : index
            hashmap[nums[i]] = i
    

        #return [-1, -1]