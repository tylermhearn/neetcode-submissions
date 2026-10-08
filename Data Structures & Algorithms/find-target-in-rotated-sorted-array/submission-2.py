class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            MID = (L + R) // 2
            if nums[MID] == target: return MID
            elif nums[L] == target: return L
            elif nums[R] == target: return R
            elif target < nums[MID] and target >= nums[L]: R = MID - 1
            else: L = MID + 1
        return -1