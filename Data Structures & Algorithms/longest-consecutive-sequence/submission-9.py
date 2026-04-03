class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Edge case when there no list return 0
        if not nums:
            return 0

        #Set the nums to remove duplicates
        numSet = set(nums)

        longestLength = 0 #check to see the longest lenght from there

        #Create a loop based on the numset
        for n in numSet:
            currentLength = 0
            if  (n - 1) not in numSet:
                while (n + currentLength) in numSet:
                    currentLength += 1
                longestLength = max(currentLength, longestLength)
        return longestLength


        #check to current num is not in the numset

        #Create a loop an increment by one until is not in the numset

        #update the lenght based on the max betweeen currentLenght, to the previous lenght


        #return the currentLength

        