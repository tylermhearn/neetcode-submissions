class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        for letter in s:
            sDict[letter] = sDict.get(letter, 0) + 1
        
        for letter in t:
          if letter not in sDict or sDict[letter] == 0:
            return False
          sDict[letter] = sDict[letter] - 1

        return True