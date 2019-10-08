class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        aStack = []
        for x in tokens:
            if x in {'+', '-', '*', '/'}:
                assert len(aStack) >= 2
                num1 = aStack.pop()
                num2 = aStack.pop()
                if x == '+':
                    aStack.append(num1 + num2)
                elif x == '-':
                    aStack.append(num2 - num1)
                elif x == '*':
                    aStack.append(num1 * num2)
                else:
                    sign = num1 * num2 >= 0
                    if num1 < 0:
                        num1 = -num1
                    if num2 < 0:
                        num2 = -num2
                    num = num2 / num1
                    if sign:
                        aStack.append(num)
                    else:
                        aStack.append(-num)
            else:
                aStack.append(int(x))
        assert len(aStack) == 1
        return aStack[0]
        
        
if __name__ == '__main__':
    mySolution = Solution()
    #input_tk = ["4","13","5","/","+"]
    input_tk = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(mySolution.evalRPN(input_tk))
