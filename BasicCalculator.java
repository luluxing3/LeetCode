public class Solution {
    
    public int calculate(String s) {
        Stack<Character> s1 = new Stack<Character>();
        Stack<Integer> s2 = new Stack<Integer>();
        s1.push('#');
        
        s += "#";
        char[] t = s.toCharArray();
        int i = 0;
        while (!s1.isEmpty()) {
            if ('0' <= t[i] && t[i] <= '9') {
                int sum = 0;
                while ('0' <= t[i] && t[i] <= '9')
                    sum = sum * 10 + t[i++] - '0';
                s2.push(sum);
            } else if (t[i] != ' ') {
                // priority in the stack is higher than that outside the stack
                if ((s1.peek() == '+' || s1.peek() == '-') && (t[i] == '+' || t[i] == '-' || t[i] == ')' || t[i] == '#')) {
                    int b = s2.pop();
                    int a = s2.pop();
                    s2.push(get(a, s1.pop(), b));
                } else if (s1.peek() == '#' && t[i] != '#'
                        || s1.peek() == '(' && t[i] != '#' && t[i] != ')'
                        || t[i] == '(') { // ... lower than ...
                    s1.push(t[i]);
                    i++;
                } else if (s1.peek() == '(' && t[i] == ')' || s1.peek() == '#' && t[i] == '#') { // both are the same priority
                    s1.pop();
                    i++;
                }
            } else {
                i++;
            }
        }
        
        return s2.pop();
    }
    
    public int get(int a, char op, int b) {
        if (op == '+') {
            return a + b;
        } else {
            return a - b;
        }
    }
}