class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a frequency counter
        freqCounter = {}

        result = []

        for i in range(len(nums)):
            freqCounter[nums[i]] = freqCounter.get(nums[i], 0) + 1
        counterFrequency = [[] for _ in range(len(nums) + 1)]
        #After that we will have counterFrequency that will have current index based on current value
        for value, index in freqCounter.items():
            counterFrequency[index].append(value)
        
        for i in range(len(counterFrequency) - 1, -1, -1):
            for s in counterFrequency[i]:
                result.append(s)
                if len(result) == k:
                    return result
