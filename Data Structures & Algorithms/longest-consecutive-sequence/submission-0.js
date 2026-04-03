class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     * case 1 when the array lenght is 0 then return 0
     * create a set with in nums to avoid duplicate
     * create a length with let
     * Traverse a loop where num of nums
     * Check to make sure num-1 is not in the set and if it in a set then skip
     * if it is true then we update num and update to make sure num + 1 has element increment the length and the num
     * update the maxLength 
     * return 0
     */
    longestConsecutive(nums) {
        //case 1
        if(nums.length === 0) return 0

        //rest is the case
        const unique = new Set(nums) // avoiding duplicate of Int
        let maxLength = 0
        for(let num of unique)
        {
            if(!unique.has(num - 1))
            {
                let currentLength = 1
                let currentnum = num
                while(unique.has(currentnum + 1))
                {
                    currentnum += 1;
                    currentLength += 1
                }
                maxLength = Math.max(maxLength, currentLength)
            }
        }
        return maxLength;
    }
}
