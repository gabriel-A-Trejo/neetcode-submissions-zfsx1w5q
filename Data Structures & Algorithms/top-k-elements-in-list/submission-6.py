class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we use frequency counter to count the number based on key and then value
        # Now we create a frequency that flips value to key and key to value to find the max frequency
        # Traverse the frequency in reverse and check to result is equal to the new value on it.
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        #swapping
        frequency = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            frequency[value].append(key)
        res = []
        for i in range(len(frequency) - 1, 0 , -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

        