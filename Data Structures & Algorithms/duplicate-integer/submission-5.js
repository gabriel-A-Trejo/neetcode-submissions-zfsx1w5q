class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const isUnique = new Set();
        for(const num of nums)
        {
            if(isUnique.has(num))
            {
                return true;
            }
            isUnique.add(num);
        }
        return false;
    }
}
