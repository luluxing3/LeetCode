class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = []
        curr_left_max = 0
        for i in range(len(height)):
            curr_left_max = max(curr_left_max, height[i])
            left_max.append(curr_left_max)
        #print(left_max)
        #print(len(left_max))
        right_max = [0] * len(height)
        curr_right_max = 0
        for i in range(len(height) - 1, -1, -1):
            curr_right_max = max(curr_right_max, height[i])
            right_max[i] = curr_right_max
        #print(right_max)
        #print(len(right_max))
        water = 0
        #print('----')
        for i in range(len(height)):
            add = min(left_max[i], right_max[i]) - height[i]
            #print('index %s add %s' %(i, add))
            water += min(left_max[i], right_max[i]) - height[i]
        #print('----')
        return water


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            
            
            
