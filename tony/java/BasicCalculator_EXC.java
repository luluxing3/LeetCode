public class Solution {
    
    private char[] operators = {'+', '-', '(', ')', '#'};
    private int[] in = {3, 3, 1, 6, 0};
    private int[] out = {2, 2, 6, 1, 0};
    
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
                if (compare(s1.peek(), t[i]) == 1) {
                    int b = s2.pop();
                    int a = s2.pop();
                    s2.push(get(a, s1.pop(), b));
                } else if (compare(s1.peek(), t[i]) == -1) {
                    s1.push(t[i]);
                    i++;
                } else {
                    s1.pop();
                    i++;
                }
            } else {
                i++;
            }
        }
        
        return s2.pop();
    }
    
    public int compare(char c1, char c2) {
        int i = indexOf(c1);
        int j = indexOf(c2);
        
        if (in[i] > out[j]) {
            return 1;
        } else if (in[i] < out[j]) {
            return -1;
        } else {
            return 0;
        }
    }
    
    public int indexOf(char c) {
        switch (c) {
            case '+' : return 0;
            case '-' : return 1;
            case '(' : return 2;
            case ')' : return 3;
            default : return 4;
        }
    }
    
    public int get(int a, char op, int b) {
        if (op == '+') {
            return a + b;
        } else {
            return a - b;
        }
    }
}