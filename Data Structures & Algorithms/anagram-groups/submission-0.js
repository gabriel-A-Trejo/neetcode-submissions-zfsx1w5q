class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     * create an object 
     * create a for loop with lower case alphabet
     * create an c to s 
     * Create a map
     * create for loop for the string
     * then create a coun with new array(26). fill0
     * for const char of str and count number of characters
     * then create a unique key with join(#)
     * !map does not have the key then return the value empthy
     * else map.get.key push str
     * Array.from(map.values())
     * 
     */ 
    groupAnagrams(strs) {
        const map = new Map()
        for (const str of strs)
        {
            const count = new Array(26).fill(0)
            for(const char of str)
            {
                count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++
            }

            const key = count.join("#")

            if(!map.has(key)) map.set(key, [])

            map.get(key).push(str)
        }
        return Array.from(map.values())
    }
}
