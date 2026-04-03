class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     * first create a new map to which is the key is the  num and value is the index
     * first create a for loop to see and we can able to see if the index is the same
     * if it is true then we will return [ , ]
     * then add the set with (current key and map)
     * last is return [-1, -1]
     */

    twoSum(nums, target) {
        const map = new Map()
        for(let i = 0; i < nums.length; i++)
        {
            let complement = target - nums[i];
            if(map.has(complement))
            {
                return[i, map.get(complement)]
            }
            map.set(nums[i], i)
        }
        return [-1, -1]
    }
}
