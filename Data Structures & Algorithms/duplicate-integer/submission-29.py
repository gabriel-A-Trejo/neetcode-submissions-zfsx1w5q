class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create an array nums return only if appears once then a set check if is in set then we return True else return false when the loop end
        isSeen = set()
        for num in nums:
            if num in isSeen:
                return True
            isSeen.add(num)
        return False

        