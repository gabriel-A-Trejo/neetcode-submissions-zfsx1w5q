from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        result = []

        # Count frequencies
        for num in nums:
            count_nums[num] = 1 + count_nums.get(num, 0)

        # Create buckets: index = frequency
        updated_list_frequency = [[] for _ in range(len(nums) + 1)]
        for num, freq in count_nums.items():
            updated_list_frequency[freq].append(num)

        # Collect top k frequent
        for i in range(len(updated_list_frequency) - 1, 0, -1):
            for num in updated_list_frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
