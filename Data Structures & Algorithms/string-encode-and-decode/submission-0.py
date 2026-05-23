class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        string = ""
        for s in strs:
          string = string + str(len(s)) + "#" + s

        return string
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strings = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter to get the length
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length and convert to int
            length = int(s[i:j])
            
            # Move past the '#'
            i = j + 1
            
            # Extract the string of that length
            strings.append(s[i:i+length])
            
            # Move past the string we just read
            i += length
        
        return strings