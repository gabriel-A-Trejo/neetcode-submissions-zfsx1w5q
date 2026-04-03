class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input: list[int] and k: int
        #edge case:
        #nums if nums empty then return []
        if not nums: return []

        counter = {}

        #Step 1: count Frequency
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        #I am thinking we can able to count the frequency based on the values 
        #so the max frequency will be switch by a list since we can order counter based on 
        #frequency to counter.
        #What if the range of nums == len of nums then we must make sure there is a plus 1
        freq = [[] for i in range(len(nums) + 1)]
        #traverse the counter
        for key, value in counter.items():
            freq[value].append(key)

        result = []

        #for the freq we can able reverse back to front
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:    
                    return result



    

        #output: list[int]        