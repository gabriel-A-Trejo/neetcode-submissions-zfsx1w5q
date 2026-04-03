class Solution {
    /**
     * Design
     * Create a map data structure the key will the value of the array and 
     * value is the index.
     * Traverse the array and create a loop where we can able to find the complement 
     * if we complement is not undefine then return the index and index of the complement.
     * if not we will add the value and the index
     * When it finish return [-1, -1]
     * 
     * 
     * 
     * 
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()
        for(let i = 0; i < nums.length; i++)
        {
            let complement = target - nums[i];
            if(map.has(complement))
            {
                return [i, map.get(complement)]
            }
            map.set(nums[i], i)
        }
        return [-1, -1]
        
    }
}
