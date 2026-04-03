class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # L will be the number of piles based on 1
        # R will based on the max Piles

        l, r = 1, max(piles)

        #create an result data structure base on it to get the min
        #while l <= r
        result = 0

        while l <= r:
            mid = (l + r) // 2

            totalSum = sum(math.ceil(pile/mid) for pile in piles)

            if totalSum <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result



        # k will be the mid and we calculate again based on the mid