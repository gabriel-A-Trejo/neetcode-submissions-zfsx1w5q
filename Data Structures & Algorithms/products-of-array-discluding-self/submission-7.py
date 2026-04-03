class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first we need to create a new type array that will intialize everything to one since we multiplying
        result = [1] * len(nums)

        #First we put prefix as  one since we need to multiple as but by the current Num[i]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        #Then reverse the loop multiply the postfix and intilize postfix by 1
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
             result[i] *= postFix
             postFix   *= nums[i]

        return result

        # then multiply by postfix hased on the result
        # then again we multiply based on the postfix
        