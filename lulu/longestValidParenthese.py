class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    if i - dp[i - 1] > 0 and s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i-1] >= 2 else 0) + 2
            max_len = max(max_len, dp[i])
        return max_len

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-last)
                    else:
                        maxlen = max(maxlen, i-stack[len(stack)-1])
        return maxlen

		#start = 0
		#max_len = 0
		#stack = [-1]
		#for index in range(len(s)):
		#	if s[index] == '(':
		#		stack.append(index)
		#	else:
		#		if len(stack) == 1:
		#			stack.pop()
		#			max_len = max(max_len, index - start + 1)
		#		elif len(stack) > 1:
		#			start_index = stack.pop()
		#			max_len = max(max_len, index - start_index + 1)
		#		else:
		#			#len(stack) == 0
		#			start = index + 1
		#return max_len
		
					

