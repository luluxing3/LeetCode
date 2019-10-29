class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        maxArea = -float('inf')
        while start < end:
            maxArea = max(maxArea, min(height[start], height[end]) * (end - start))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return maxArea

            
