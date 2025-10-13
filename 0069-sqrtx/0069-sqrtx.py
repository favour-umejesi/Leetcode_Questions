class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Using binary search over a range of 
        """
        first, last = 1, x
        if x is 0:
            return 0
        
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid

            elif mid > x // mid:
                last = mid - 1

            else:
                first = mid + 1
        
        return last