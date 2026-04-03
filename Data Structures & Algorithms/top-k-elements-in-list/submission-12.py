class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Edge case will be when not nums reuturn an empty array
        if not nums: return []
        #Have an array as an result [] which get us the top k elements
        result = []


        #Create counter frequency that count the values : number with that values
        frequencyCounter = {}

        for i in range(len(nums)):
            frequencyCounter[nums[i]] = frequencyCounter.get(nums[i], 0) + 1




        #After we replace theses number with that values as frequency element and
        # added based values based on a list
        # We will create a nest list 
        bucketSort = [[] for _ in range(len(nums) + 1)] #Edge when all numbers of k is equal to that number

        for index, value in frequencyCounter.items():
            bucketSort[value].append(index)



        #We will reverse a list 
        for i in range(len(bucketSort) - 1, 0, -1):
            for bucket in bucketSort[i]:
                result.append(bucket)
                if len(result) == k:
                    return result
        #We will use for loop for that list addded into result unti it equals to k then return result 
        return []

