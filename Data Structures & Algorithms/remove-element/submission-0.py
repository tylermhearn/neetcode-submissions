class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
          return 0;
        end = len(nums)
        index = 0
        while index < len(nums):
          if nums[index] == 'x':
            return index
          if nums[index] == val:
            nums[index] = nums[end-1]
            nums[end-1] = 'x'
            end = end - 1
          else:
            index = index + 1

        return index