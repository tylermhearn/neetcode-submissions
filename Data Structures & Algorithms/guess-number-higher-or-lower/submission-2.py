# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L , R = 1, n
        while L <= R:
            MID = (L + R) // 2
            if guess(MID) == 0: return MID
            elif guess(MID) == 1: L = MID + 1
            else: R = MID - 1
        return L