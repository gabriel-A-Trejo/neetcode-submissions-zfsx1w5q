class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        lengthNums = len(nums)

        
        #FIRST COUNT THE ELEMENTS
        counter = {}
        for i in range(lengthNums):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        
        #Re-order by the number of frequency
        reorderTopFrequency = [[] for _ in range(lengthNums + 1)]
        for key, value in counter.items():
            reorderTopFrequency[value].append(key)
        
        #find the top K elements
        for i in range(len(reorderTopFrequency) - 1, -1, -1):
            for topNumber in reorderTopFrequency[i]:
                result.append(topNumber)

                if len(result) == k:
                    return result
                

        