class Solution {
    /**
     * Design
     *  Test to make sure that s and t are equal length
     *  Create two maps to count the frequency
     *  Traverse to count the frequency
     *  check the key if they are the same
     * 
     * Document
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false

        let countS = new Map()
        let countT = new Map()

        for(let i = 0; i < s.length; i++)
        {
            countS.set(s[i], 1 + (countS.get(s[i]) || 0))
            countT.set(t[i], 1 + (countT.get(t[i]) || 0))
        }

        for(let [key, value] of countS)
        {
            if(value !== countT.get(key))
            {
                return false
            }
        }

        return true
    }
}
