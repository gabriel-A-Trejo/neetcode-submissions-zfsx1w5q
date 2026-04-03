class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First step is to do a frequency counter
        #NExt step is to create a counter based of the lenght of the list since it can up to n 
        #Swap the values and keys from since depending on the number of frequency on that is based on [] which can able to have multiple in that list for them
        #After that reverse traverse

        counter = {}
        for num in nums:
             counter[num] = 1 + counter.get(num, 0)
        frequency = [[] for i in range(len(nums) + 1)]
        for key, value in counter.items():
            frequency[value].append(key)
        res = []
        for i in range(len(frequency) - 1, -1, -1 ):
            for j in frequency[i]:
                res.append(j)
            if len(res) == k:
                return res
