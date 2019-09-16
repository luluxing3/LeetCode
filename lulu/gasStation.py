class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        _sum = 0
        total = 0
        j = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            _sum += gas[i] - cost[i]

            if _sum < 0:
                j = i
                _sum = 0

        if total >= 0:
            return j + 1
        else:
            return -1

    #######wrong###################
    #def canCompleteCircuit(self, gas, cost):
    #    """
    #    :type gas: List[int]
    #    :type cost: List[int]
    #    :rtype: int
    #    """
    #    start_index = self.findSatrt(gas, cost)
    #    if start_index != -1 and self.canCompleteCircuitFromStart(gas, cost, start_index):
    #        return start_index
    #    else:
    #        return -1
    #        
    #def canCompleteCircuitFromStart(self, gas, cost, start_index):
    #    prev_gas = 0
    #    for index in range(start_index, len(gas)):
    #        curr_gas = prev_gas + gas[index] - cost[index]
    #        if curr_gas < 0:
    #            return False
    #        prev_gas = curr_gas
    #    for index in range(0, start_index):
    #        curr_gas = prev_gas + gas[index] - cost[index]
    #        if curr_gas < 0:
    #            return False
    #        prev_gas = curr_gas
    #    print('success')
    #    return True
    #        
    #def findSatrt(self, gas, cost):
    #    last_index = -1
    #    last_pos = 0
    #    start_index = -1
    #    start_pos = 0
    #    for index in range(len(gas)):
    #        pos = gas[index] - cost[index]
    #        if pos > 0:
    #            if last_pos > 0:
    #                last_pos += pos
    #            else:
    #                last_pos = pos
    #                last_index = index
    #        else:
    #            if last_pos > start_pos:
    #                start_index = last_index
    #                start_pos = last_pos
    #            last_index = index
    #            last_pos = pos
    #        #print('-----index %s' %index)
    #        #print('last_pos: %s last_index: %s' %(last_pos, last_index))
    #        #print('start_pos: %s start_index: %s' %(start_pos, start_index))

    #    if last_pos > start_pos:
    #        start_index = last_index
    #        start_pos = last_pos
    #        last_index = index
    #        last_pos = pos
    #    print('start_index = %s' %start_index)

    #    return start_index

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(mySolution.canCompleteCircuit([2,3,4], [3,4,5]))
    print(mySolution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
    print(mySolution.canCompleteCircuit([4,5,2,6,5,3], [3,2,7,3,2,9]))
    print(mySolution.canCompleteCircuit([5,8,2,8], [6,5,6,6]))
                    
                
        
                
        
