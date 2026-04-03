class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input array int, int -> array of int index
        #Hasmap will be the way since the value will be the key and value will be the index to keep track the complement
        #return to the index if we found the target in the hashmap of the value

        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in hashmap):
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
    
        