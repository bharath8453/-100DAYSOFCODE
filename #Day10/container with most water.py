class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_area = max(max_area, area)
            
            # Move the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Example run
height = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(height)
print("Max water area:", result)