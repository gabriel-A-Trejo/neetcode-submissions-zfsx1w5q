class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        counterNum = {}
        for i in range(len(nums)):
            counterNum[nums[i]] = 1 + counterNum.get(nums[i], 0)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in counterNum.items():
            bucket[value].append(key)
        

        for i in range(len(bucket) - 1, -1, -1):
            for buck in bucket[i]:
                result.append(buck)
                if len(result) == k:
                    return result
            