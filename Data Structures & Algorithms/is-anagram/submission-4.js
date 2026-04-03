class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     * Data structure is an object the return will be value base on the count
     * first is to chekc if it is the same length
     * traverse elements and key will the char and value will an int
     * then traverse elements to both key elements are the same value count else return false
     * else true
     */
    isAnagram(s, t) {
        if(s.length !== t.length)
        {
            return false
        }
        
        const countT = {}
        const countS = {}

        for(let i = 0;  i < s.length ; i++)
        {
            countS[s[i]] = 1 + (countS[s[i]] || 0)
            countT[t[i]] = 1 + (countT[t[i]] || 0)
        }

        for(const key of s)
        {
            if(countS[key] !== countT[key] )
            {
                return false
            }
        }
        return true
    }
}
