class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first lets calculate rate of banna is eating and next is to calulate the rate of banana  based on speed on this based on it
        l, r = 1, max(piles)
        result = r
        while l <= r :
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        return result


        