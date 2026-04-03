class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Create l and R to the starting point
        l = 0
        r = len(numbers) - 1

        #Traversing the list of an array
        while l < r:
            #We will check if the sum > target then r -= 1
            while numbers[l] + numbers[r] > target:
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1 ]
            
            

        