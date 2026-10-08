class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            MID = (L + R) // 2
            if nums[MID] == target: return MID
            if nums[L] <= nums[MID]:
                # Left half is sorted
                if nums[L] <= target < nums[MID]:
                    R = MID - 1
                else:
                    L = MID + 1
            else:
                # Right half is sorted
                if nums[MID] < target <= nums[R]:
                    L = MID + 1
                else:
                    R = MID - 1
                    return -1