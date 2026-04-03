class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Edge case if nums does not exsit return -1
        #or target does not exist return -1

        if not nums : return -1

        l, r = 0, len(nums) - 1

        #Two pointer to l to right but <= 
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

        #Find mide which l + r //2
    

        #if the mid == target return the index

        #elif mid > target return r = m - 1
        #else is l = m + 1



        