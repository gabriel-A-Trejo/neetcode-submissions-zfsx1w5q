class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []


        #frequency counter
        frequency_counter = {}
        for num in nums:
            frequency_counter[num] = frequency_counter.get(num, 0) + 1
        newList = [[] for _ in range(len(nums) + 1)]
        for index, value in frequency_counter.items():
            newList[value].append(index)
        for i in range(len(newList) - 1, 0, -1):
            for num in newList[i]:
                result.append(num)
                if len(result) == k:
                    return result

            
        