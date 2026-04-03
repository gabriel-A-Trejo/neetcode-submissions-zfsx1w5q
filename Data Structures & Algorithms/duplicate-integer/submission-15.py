class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Edge case when nums is empty
        #Edge case when when returns to 0

        #Pesudo Code

        #DSA a set
        #Create a for loop and check to and check to see is already in the set
        #if is already is in the set then return True else return false when you finish traversing the for loop

        isContain = set()

        for num in nums:
            if num in isContain:
                return True
            isContain.add(num)
        return False

         