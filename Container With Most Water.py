class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the width between the two pointers
            width = right - left
            
            # The height of the water is limited by the shorter bar
            h = min(height[left], height[right])
            
            # Update max_val if the current area is larger
            current_area = width * h
            max_val = max(max_val, current_area)
            
            # Strategy: Move the pointer pointing to the shorter bar
            # because keeping the shorter bar will never produce a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_val
