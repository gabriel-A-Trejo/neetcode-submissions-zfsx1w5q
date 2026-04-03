class Solution {
    /**
     * Design
     * create data structure name set
     * traverse num and check the name that is givng has it already and if they do then return to true
     * else add towards the set and return it false
     */

    /*
    * @Param ({nums : number[]})
    * return ({bool})
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
        return false
    }
        
}
