class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:  # Use `<=` to ensure all elements are considered
            mid = l + (r - l) // 2  # Correct calculation for mid
            if nums[mid] > target:
                r = mid - 1  # Move the right pointer to `mid - 1`
            elif nums[mid] < target:
                l = mid + 1  # Move the left pointer to `mid + 1`
            else:
                return mid  # Return the index if target is found
        return -1  # Return -1 if the target is not in the array

        