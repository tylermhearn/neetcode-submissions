class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            MID = (L + R + 1) // 2
            if nums[MID] == target: return MID
            elif nums[MID] <= target:
                L = MID + 1
            else: R = MID - 1
        if target < nums[MID]: return MID - 1
        else: return MID + 1