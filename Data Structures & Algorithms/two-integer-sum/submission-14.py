class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input is list ints and target of int
        #output: list of ints

        #edge cases:
        #nums is empty return []
        if not nums: return []

        #DSA: will be a dictionary of values:index
        hashmap = {}

        #iterate throught the list i range for loop 

        #Another good way is to see if target - current[i] which we called complement
        #check to if complement in  hashmap is in there then return indexs 
        

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        