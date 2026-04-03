class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      sFrequency = {}
      tFrequency = {}

      if len(s) != len(t):
        return False 

      for i in range(len(s)):
        sFrequency[s[i]] = sFrequency.get(s[i], 0) + 1
        tFrequency[t[i]] = tFrequency.get(t[i], 0) + 1   
      return sFrequency == tFrequency