class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Edge cases when nums list is empty and target is also empty
        #Edge case 2 will be when target is not found which return -1


        # if mid is less then the target the l will be updated to l = m + 1
        # if mid is greater then the target then r will be r = m
        # if target == mid then return mid

        #first i think is to create a while loop where l <= r:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1