class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # two pointers: left and right

        while l < r:
            currentSum = numbers[l] + numbers[r]  # sum of current pair
            if currentSum == target: 
                return [l + 1, r + 1]  # return 1-based indices
            elif currentSum > target:
                r -= 1  # sum too big, move right pointer left
            else:
                l += 1  # sum too small, move left pointer right
        return []  # no solution found
        