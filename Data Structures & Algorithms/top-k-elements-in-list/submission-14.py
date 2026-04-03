class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create counter frequency
        counterFrequency = {} #Value: counter

        for i in range(len(nums)):
            counterFrequency[nums[i]] = counterFrequency.get(nums[i], 0) + 1

        #We need a list of list where is + 1 when there all of elements has the same number
        indexToValue = [[] for _ in range(len(nums) + 1)]
        for value, index in counterFrequency.items():
            indexToValue[index].append(value)

        result = []

        #reverse the loop based on indexToValue
        for i in range(len(indexToValue) - 1, -1, -1):
            for num in indexToValue[i]:
                result.append(num)
                if k == len(result):
                    return result


        