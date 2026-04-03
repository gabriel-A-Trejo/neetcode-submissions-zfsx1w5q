class Solution:
    def findMin(self, nums: List[int]) -> int:
        #We are finding the minimum based on the sorted Array based on it
        #set the result to byt nums[0]
        #initlaiz l adn r by first by 0 and the other by len list by - 1
        result = nums[0]
        l, r = 0, len(nums) - 1


        #Create a while lopp based on the pattern

        #Check to see if l <= r: then set to nums based on the min
        while l <= r:

            if nums[l] <= nums[r]:
                result = min(result, nums[l])
                break
            mid = (l + r) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r =  mid - 1
        return result


        # create the mid point

        # then we update the ereuslt based on the min

        #then we check if l >= right based on nums
        #then we set to the left
        #Else right based on it




        


        