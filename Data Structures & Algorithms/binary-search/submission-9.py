class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #plan
        """
        Plan
        Using two pointers
        Traversing when l <= r
        find the mid point in the binary search

        check to if target else decerement r or increment l based on mid points

        """

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1