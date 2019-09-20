import sys
INTMAX = sys.intmax
class Solution(object):
    def string2int(self, string):
        start_index, isValid, isPositive = self.preprocess(string)
        if isValid:
            int_num = 0
            for i in range(start_index, len(string)):
                if string[i].isdigit():
                    if int_num > INTMAX / 10 and string[i] > INTMAX/10 - int_num/10:
                        int_num = INTMAX
                        break
                    else:
                        int_num = 10 * int_num + int(string[i])
             if isPositive:
                return int_num
             else:
                return int_num * (-1)
        else:
            return 0
           
    def preprocess(self, string):
        #retrun string is valid or not; negative or positive
        start_index = None
        isValid = None
        isPositive = None
        for i in range(len(string)):
            if string[i].isdigit() or string[i] in ['+', '-']:
                start_index = i
                break
        if i:
            if string[start_index] == '-':
                isPositive = False
                start_index = i + 1
            elif string[start_index].isdigit():
                isPositive = True
                isValid = True
                start_index = i
            else:
                isPositive = True
                for i in range(start_index+1, len(string)):
                    if string[i].isdigit():
                        isValid = True
                        break
                if isValid is None:
                    isValid = False
                start_index = i + 1
        return start_index, isValid, isPositive


