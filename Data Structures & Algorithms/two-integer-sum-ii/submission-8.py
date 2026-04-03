class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Same pattern

        l, r = 0, len(numbers) - 1

        while l < r:
            #Current sum
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l + 1, r + 1]
            elif currentSum < target:
                l += 1
            else:
                r -= 1
    

        
        