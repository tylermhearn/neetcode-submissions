class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      hmap = {}
      for string in strs:
        counts = [0] * 26
        for letter in string:
          counts[ord(letter) - ord('a')] = counts[ord(letter) - ord('a')] + 1
        my_tuple = tuple(counts)
        array = hmap.get(my_tuple, [])
        array.append(string)
        hmap[my_tuple] = array

      return list(hmap.values())