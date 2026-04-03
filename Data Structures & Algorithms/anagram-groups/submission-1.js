class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     * Create a map
     * for loop with str and create array fill until 26
     * create inner loop for the char and count[with the char - a] which will be added as ++;
     * create key that is unique that has count.join("#")
     * if does not have key then leve it empety 
     * ans[key].push(s)
     * return values
     */
    groupAnagrams(strs) {
        const map = new Map()
        for(const str of strs)
        {
            const count = Array(26).fill(0)
            for(const char of str)
            {
                count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++
            }

            const key = count.join("#");

            if(!map.has(key)) {
                map.set(key, [])
            }
            map.get(key).push(str)
        }
        return Array.from(map.values())
    }
}
