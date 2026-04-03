class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map()
        for(let i = 0; i < nums.length; i++)
        {
            map.set(nums[i], (map.get(nums[i]) || 0) + 1)
        }
        const sorted = [...map.entries()].sort((value1, value2) => value2[1] - value1[1]);
        const result = sorted.slice(0, k).map(entry => entry[0]);

        return result
    }
}
