class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        result = []

        if k < 0:
            return [-1]

        #count the frequency
        countNums = {}
        for i in range(lenNums):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0) 

        OrderTheFrequency = [[] for _ in range(lenNums + 1)]
        for index, value in countNums.items():
            OrderTheFrequency[value].append(index)
        
        for i in range(len(OrderTheFrequency) -1, 0, -1):
            for num in OrderTheFrequency[i]:
                result.append(num)
                if len(result) == k: 
                    return result

        

        
        