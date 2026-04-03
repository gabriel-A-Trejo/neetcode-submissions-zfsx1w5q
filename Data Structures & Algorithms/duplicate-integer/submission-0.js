class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
       let isUnique = new Set();
       for(const num of nums)
       {
        if(isUnique.has(num)) return true;
        else isUnique.add(num)
       }
       return false
    }
}
