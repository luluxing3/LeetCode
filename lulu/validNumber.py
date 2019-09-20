class Solution(object):
    def isValidNumber(self, string):
        string = string.strip()
        if not string:
            return False
        
        if string[0] in ['+', '-']:
            return self.isValidNumber(string[1:])
        else:
            isFloat = False
            isE = False
            for i in range(len(string)):
                if not string[i].isdigit():
                    if string[i] == 'e' and not isE:
                        isE = True
                    elif string[i] == '.' and not isFloat:
                        isFloat = True
                    else:
                        return False
            return True

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.isValidNumber('  c12e32e'))
                    
            
