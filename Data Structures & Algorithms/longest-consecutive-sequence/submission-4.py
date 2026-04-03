class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Each element is exactly 1 greater then the previous element and the array does not have to be consecutive
        # input: [2, 20, 4, 10, 3, 4, 5]
        # output: 4

        #Example 2: input[5, 4, 3, 8, 9, 10]     
        #output 3

        #DSA: set

        #if there is no nums then return 0
        if not nums: return 0

        uniqueNums = set(nums) 
        longest = 1

        for num in  uniqueNums:
            if num - 1 not in uniqueNums:
                currentLength = 1
                while (num + currentLength) in uniqueNums:
                    currentLength += 1
                longest = max(currentLength, longest )
        return longest

