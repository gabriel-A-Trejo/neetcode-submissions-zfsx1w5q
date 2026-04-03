class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        return nums.reduce((acc, num, i) => {
            const complement = target - num;
            if (map.has(complement)) return [map.get(complement), i];
            map.set(num, i);
            return acc;
        }, []);
    }

    }

