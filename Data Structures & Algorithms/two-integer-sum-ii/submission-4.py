class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

     
        while l < r:
            currentSum = numbers[r] + numbers[l]
            if currentSum == target:
                return [l + 1, r + 1]
            elif currentSum > target:
                r -= 1
            else:
                l += 1
        