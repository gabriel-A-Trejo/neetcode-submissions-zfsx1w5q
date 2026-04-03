class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // Create a Set from the array
        const isUnique = new Set(nums);
        // Compare the size of the Set to the length of the array
        return isUnique.size !== nums.length;
    }
}
