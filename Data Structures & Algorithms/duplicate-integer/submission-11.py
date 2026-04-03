class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Traversse and to see if there is duplicated by creating a code if contains duplicate return true
        isContain = set()
        for num in nums:
            if num in isContain:
                return True
            isContain.add(num)
        return False



         