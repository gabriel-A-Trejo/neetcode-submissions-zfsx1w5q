class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #First we need to create an hashmap to determin based on value: key

        hashmap = {}

        #next thing create for loop where length nums
        for i in range(len(nums)):

        #Create a complement based on the target - current index poistion
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

        #check to see if complement is alreayd in the hasmap 
            hashmap[nums[i]] = i
        #if it then return coplement, i

        #added the current value to the current key
        