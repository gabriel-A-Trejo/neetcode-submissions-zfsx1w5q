class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        const counter = new Map();

        for(let i = 0; i < s.length ; i++)
        {
            counter.set(s[i], (counter.get(s[i]) || 0 ) + 1)
            counter.set(t[i], (counter.get(t[i]) || 0 ) - 1)
        }

        return [...counter.values()].every(value => value === 0)
    }
}
