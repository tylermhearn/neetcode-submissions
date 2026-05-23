class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      output = []
      dict1 = {}
      for string in strs:
        array = dict1.get(tuple(sorted(string)), [])
        array.append(string)
        dict1[tuple(sorted(string))] = array

      return list(dict1.values())