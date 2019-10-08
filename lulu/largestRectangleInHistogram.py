class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []
        i = 0
        while i < len(heights):
            if len(stack) == 0 or stack[-1] <= heights[i]:
                stack.append(heights[i])
            else:
                count = 0
                while len(stack) > 0 and stack [-1] > heights[i]:
                    count += 1
                    maxArea = max(maxArea, stack[-1] * count)
                    stack.pop()
                while count > 0:
                    count -= 1
                    stack.append(heights[i])
                stack.append(heights[i])
            i += 1
        
        count = 1
        while len(stack) != 0:
            maxArea = max(maxArea, stack[-1] * count)
            count += 1
            stack.pop()
            
        return maxArea
            

