class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1, 2, 3, 3] it contains only when there is multiple of the same number
        # [1, 2, 3, 4] this is false since there is not the same number

        #BruteForce is worst case (n)
        #input is a list of ints which the output is checking point to see if true or false it contains more then one number which is a searching problem.
        #DSA: will be a set
        seen = set()

        #First we will traverse to see if the set is already has it in else it will be false
        for i in range(len(nums)):
            isSeen = nums[i] in seen
            if(isSeen): return True
            seen.add(nums[i])
        return False
        
