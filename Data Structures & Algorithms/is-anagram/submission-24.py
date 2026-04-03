class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False
        
        s_count_frequency = {}
        t_count_frequency = {}

        for i in range(s_length):
            s_count_frequency[s[i]] = 1 + s_count_frequency.get(s[i], 0)
            t_count_frequency[t[i]] = 1 + t_count_frequency.get(t[i], 0)
        return s_count_frequency == t_count_frequency
        