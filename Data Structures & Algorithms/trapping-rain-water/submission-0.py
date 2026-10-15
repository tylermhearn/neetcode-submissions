class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        L , R = 0, len(height) - 1
        lMax, rMax = 0, 0
        while L < R:
            if lMax < rMax:
                
                L += 1
                lMax = max(lMax, height[L])
                total += lMax - height[L]
            else:
                R -= 1
                rMax = max(rMax, height[R])
                total += rMax - height[R]
        return total