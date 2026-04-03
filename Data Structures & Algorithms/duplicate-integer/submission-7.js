class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     * data structure will be set
     * for loop and to check if the set already has it already if does return true else add it to the set
     * return false whhen the loop finish
     */
    hasDuplicate(nums) {
        const isSet = new Set()
        for(const num of nums)
        {
            if(isSet.has(num)) return true;
            isSet.add(num)
            
        }
        return false
    }
}
