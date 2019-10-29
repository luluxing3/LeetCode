class Solution(object):
    def jump(self, nums):
        reach = 0
        step = 0
        i = 0
        while i <= reach:
            if reach >= len(nums) - 1:
                return step
            nextReach = 0
            for index in range(i, reach + 1):
                nextReach = max(nextReach, nums[index] + index)
            step += 1
            i = index + 1
            reach = nextReach
        return None
