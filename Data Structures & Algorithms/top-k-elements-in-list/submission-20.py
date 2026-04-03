class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        if k <= 0:
            return [-1, -1]

        #count the frequency
        countNums = {}
        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)
        
        #create 2d array to re-order based on the count frequency
        orderFrequentElement = [[] for _ in range(len(nums) + 1)]
        for index, value in countNums.items():
            orderFrequentElement[value].append(index)
        
        #reverse the loop get the highest frequency
        for i in range(len(orderFrequentElement) - 1, 0, -1):
            for element in orderFrequentElement[i]:
                result.append(element);
                if len(result) == k:
                    return result

        