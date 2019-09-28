class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #skip whitespaces
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        #sign
        sign = 1
        if i<len(str) and (str[i]=='+' or str[i]=='-'):
            if str[i]=='-': sign=-1
            i += 1
        #sum
        sum = 0
        while i<len(str) and ord(str[i])>=ord('0') and ord(str[i])<=ord('9'):
            if sum > (2**31-1) / 10 or int(str[i]) > (2**31-1) - 10*sum:
                sum = 'inf'
                break
            else:
                sum = sum*10 + int(str[i])
                i += 1
        if sum == 'inf':
            if sign == 1:
                return 2**31-1
            else:
                return -2**31
        else:
            return sum * sign
