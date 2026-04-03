class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        You are given an integer array piles where piles[i] is the
        number of bananas in the ith pile. 
        You are also given an integer h, which represents the number of
        hours you have to eat all the bananas.
        """

        #My thinking since we looking for mininum we should focus on the left
        # FInd the what is left and right this will be 1 and max of piles
        # then we calculate the mid 
        # we will sum the the piles and check to see if it works based on it

        l, r = 1, max(piles)

        result = 0

        while l <= r:
            mid = (l + r) // 2

            totalSum = sum(math.ceil(pile / mid) for pile in piles)

            if totalSum <= h:
                result = mid
                r = mid - 1

            else:
                l = mid + 1
        return result


        """
        You may decide your bananas-per-hour eating rate of k.
        Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
        If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
        """
        #total sum <= h 
        # we result = total sum
        # move it to the down by r = mid - 1
        #else l = mid + 1

        #return Result
        