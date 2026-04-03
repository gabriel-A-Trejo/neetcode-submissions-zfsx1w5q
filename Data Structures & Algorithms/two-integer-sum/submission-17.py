class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input list of ints, int
        

        #example: [1, 1] target 1 then it will be return based on the indeces
        # so will be like value: index
        #example2: []  target 2 this will be undefine
        #example3: [1, 2, 3, 4] target is 5 then traversing the list then check to if we already have the value based another way we can able to do is substract then target with the current index and we check to see if it already contains hashmap from value: index

        #interviewer question: all ints are integares when n >= 0
        #another question can it contain negative numbers in the list and the target

        #edge case if nums is empty and target is empty then return []
        #DS: dictionary based on value:index
        #algorithm
        # first step is edge case
        #second step is to intitialize the hashmap where will be the key is the value and value is the index from the list
        #final step is check to see if it target currenlty substracts with current value and check to see if the it contains in the dictionraru if is true then return [index from hashmap, index]

      
        
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in hashmap ):
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        
    
        

        #output list of ints
        