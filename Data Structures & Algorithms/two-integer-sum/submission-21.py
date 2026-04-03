class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create an hashmap to check the current value : indexes

        hashmap = {}

        #Create for loop where we get the current index
        for i in range(len(nums)):
            complement = target - nums[i]
            if  complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        #Then we substract the target - current value
        #Check to see if the complement in the hashmap then return index based on ocmplement with current index
        #add the current value based on index

    