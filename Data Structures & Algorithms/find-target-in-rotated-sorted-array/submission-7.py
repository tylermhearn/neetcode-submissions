class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            MID = (L + R) // 2
            if nums[MID] == target: return MID
            elif nums[MID] < nums[R]:
                if target > nums[MID]: L = MID + 1
                else: R = MID - 1
            else:
                if target > nums[MID]: R = MID - 1
                else: R = MID + 1
        return -1