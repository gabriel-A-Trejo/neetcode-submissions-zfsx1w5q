class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Handle edge case
        if k <= 0:
            return [-1]

        # Step 1: Count the frequency of each number
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Step 2: Create a frequency list (bucket sort)
        frequency = [[] for _ in range(len(nums) + 1)]
        for key, value in counter.items():
            frequency[value].append(key)

        # Step 3: Collect the top k frequent elements
        res = []
        for i in range(len(nums), 0, -1):  # Start from the highest frequency
            for key in frequency[i]:
                res.append(key)
                if len(res) == k:  # Stop when we have k elements
                    return res

        return res  # In case k > unique elements (this may return less than k items)


            