class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     * 
     * also check the length of the string just in case is correct amount.
     * first step is we can able to create two objects that key will be character of the name and there will be two count
     * 0 + 1 if it is true  else false then 1 + 1 = 2
     * then check all key base if all tha value is the same
     * 
     */

    isAnagram(s, t) {
        if (s.length !== t.length) return false

        const countT = {}
        const countS = {}

        for(let i = 0; i < s.length ; i++)
        {
            countS[s[i]] = 1 + (countS[s[i]] || 0)
            countT[t[i]] = 1 + (countT[t[i]] || 0)
        }

        for(const key of s)
        {
            if(countT[key] !== countS[key])
            {
                return false
            }
        }
        return true
    }
}
