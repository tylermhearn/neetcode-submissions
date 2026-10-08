class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 1, x
        while L <= R:
            MID = (L + R) // 2
            SQUARE = MID * MID
            if SQUARE == x: return MID
            elif SQUARE > x: R = MID - 1
            else: L = MID + 1
        return R