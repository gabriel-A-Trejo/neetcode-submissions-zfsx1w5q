class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We called it result as an array
        result = []

        counter = {}

        #We use a count frequency and count number of the times based on the value
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        reverseCounter = [[] for _ in range(len(nums) + 1)]

        #Then we will switch to and it will become index : value for it
        for value, index in counter.items():
            reverseCounter[index].append(value)
        
        for i in range(len(reverseCounter) - 1, -1, -1):
            for num in reverseCounter[i]:
                result.append(num)
                if len(result) == k:
                    return result

        #Create for loop but in reverse and and create for loop just in case there more then one inside that list
        #return only when is len of result == to k
        