class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #We will use two pointer method l , r = 0, len(numbers) - 1
        if not numbers:
            return [-1, -1]

        l, r = 0, len(numbers) - 1

        

        #Create a while loop where l < r:
        while l < r:
            

        # check the current sum by summing s[l] + s[r]:
            currentSum = numbers[l] + numbers[r]

        #check to see if current sume to target then return [l, r]
            if currentSum == target:
                return [l + 1, r + 1]

        #if the current sum is grater then the target then we decrement r
            elif currentSum > target:
                r -= 1

        #else: we increment 1
            else: 
                l += 1

        #Result [-1, -1 ] when the target is not found or when numbers does not exist
        return [-1, -1]


        