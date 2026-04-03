class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: nums: [1, 2, 2, 3, 3, 3] and k: 2
        # output: [2, 3]

        #DSA: returning a list, but we will use a hashmap for a counter
        #Algo: Based on k it will be max of the counter so if we have 3 thress and two to twos the max will 3 and max will be 2 but we must check
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res