class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #We use an hashset for this 

        #we set as nums in the hash set
        # create a for loop check to see if the num -1 is hashset if is not  then we will create a while loop that [nums + length] inside hashent return maxvalue of the output
        hashSet = set(nums)
        result = 0

        for num in hashSet:
            if num - 1 not in hashSet:
                length = 1
                while num + length in hashSet:
                    length += 1
                result = max(result, length)
        return result 
        