class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
          return 0;
        read, write = 0, 0
        while read < len(nums):
          if nums[read] != val:
            nums[write] = nums[read];
            read = read + 1
            write = write + 1
          else:
            read = read + 1
        return write;