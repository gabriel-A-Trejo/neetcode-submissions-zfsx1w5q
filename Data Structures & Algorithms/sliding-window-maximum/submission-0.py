class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        countIndex = collections.deque()
        l = 0

        for r in range(len(nums)):
            while countIndex and  nums[countIndex[-1]] < nums[r]:
                countIndex.pop()
            countIndex.append(r)

            if l > countIndex[0]:
                countIndex.popleft()
            
            if (r + 1) >= k:
                output.append(nums[countIndex[0]])
                l += 1
        return output



        