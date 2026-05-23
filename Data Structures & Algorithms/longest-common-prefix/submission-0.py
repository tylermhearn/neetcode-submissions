class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      hmap = {}
      for s in strs:
        for index in range(len(s)):
          hmap[s[:index+1]] = hmap.get(s[:index+1], 0) + 1   
      # Find longest prefix that appears in all strings
      longest_prefix = ""
      for prefix, count in hmap.items():
          if count == len(strs) and len(prefix) > len(longest_prefix):
              longest_prefix = prefix
      return longest_prefix