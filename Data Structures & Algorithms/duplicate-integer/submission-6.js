class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */

    /*
    first is declare a set since it only contains unique values
    First step is to iterate by using a for loop
    Check to see if the num inside loop has it already in the same and if does then return true 
    then add the set the number if it is false.
    at end of the loop return false if everything is unique
    

    */
    hasDuplicate(nums) {
        const isUnique = new Set();
        for(const num of nums)
        {
            if(isUnique.has(num))
            {
                return true
            }
            isUnique.add(num)
        }
        return false;
    }
}
