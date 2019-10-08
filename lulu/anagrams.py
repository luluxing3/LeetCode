class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in ans:
                ans[sorted_s].append(s)
            else:
                ans[sorted_s] = [s]
        return ans.values()
