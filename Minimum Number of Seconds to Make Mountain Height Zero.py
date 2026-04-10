import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def can_reduce(max_time):
            total_height_reduced = 0
            for w in workerTimes:
                # Calculate max k such that w * k * (k + 1) / 2 <= max_time
                # Solving k^2 + k - (2 * max_time / w) <= 0
                k = int((-1 + math.sqrt(1 + 8 * max_time // w)) // 2)
                total_height_reduced += k
                if total_height_reduced >= mountainHeight:
                    return True
            return total_height_reduced >= mountainHeight

        # Binary search for the minimum time
        low = 1
        # Upper bound: fastest worker doing the whole mountain
        fastest_worker = min(workerTimes)
        high = fastest_worker * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
