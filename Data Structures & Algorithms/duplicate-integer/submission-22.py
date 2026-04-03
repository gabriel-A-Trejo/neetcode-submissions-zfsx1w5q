class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #let see if there no nums then return false if nothing in th elist
        if not nums:
            return False
        #Create a hashmap to keep track the previous numbers from the loop
        hashset = set()

        #create a loop where i is in the range of nums[i] - 1 of the lenght
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        #check the current psotion to see if the value of that position is already in the hashset 
        #return true or other conitnue and added in the hashset

        #when loops end return False since we dont have have a duplciate
        