class Solution:
    def search(self, nums: List[int], target: int) -> int:
       l, r = 0, len(nums) - 1 #Two pointer Pattern

       while l <= r: #Two pointer pattern but except <=
              mid = (l + r) // 2

              if nums[mid] == target:
                     return mid
              elif nums[mid] < target:
                     l = mid + 1
              else:
                     r = mid - 1
       return -1

        