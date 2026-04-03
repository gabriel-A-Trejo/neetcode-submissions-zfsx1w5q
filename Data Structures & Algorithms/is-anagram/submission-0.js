class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // Check if the strings are of different lengths
        if (s.length !== t.length) return false;

        const counter = new Map();

        // Traverse both strings
        for (let i = 0; i < s.length; i++) {
            // Increment count for characters in s
            counter.set(s[i], (counter.get(s[i]) || 0) + 1);
            // Decrement count for characters in t
            counter.set(t[i], (counter.get(t[i]) || 0) - 1);
        }

        // Check if all counts are zero
        return [...counter.values()].every(value => value === 0);
    }
}