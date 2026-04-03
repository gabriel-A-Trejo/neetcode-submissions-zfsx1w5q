class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index_by_value = {}
        mostFrequentNumber = []
        for num in nums:
             index_by_value[num] = 1 + index_by_value.get(num, 0)

        length = len(nums)
        buckets = [[] for _ in range(length + 1)]
        for currentValue, frequency in index_by_value.items():
            buckets[frequency].append(currentValue)
        for frequency in range(length, 0, -1):
            for HighNumber in buckets[frequency]:
                mostFrequentNumber.append(HighNumber)
                if len(mostFrequentNumber) == k:
                    return mostFrequentNumber
            

        
        