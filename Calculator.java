import java.util.Stack;

public class Calculator {
	
	private char[] opreators = {'+', '-', '*', '/', '(', ')', '#'};
	private int[] in = {3, 3, 5, 5, 1, 6, 0}; // priority in the stack
	private int[] out = {2, 2, 4, 4, 6, 1, 0}; // priority out of the stack
	
	public static void main(String args[]) {
		Calculator calculator = new Calculator();
		System.out.println(calculator.calculate("(2+3*4/2)*4-1*2"));
	}
	
	public int calculate(String s) {
		Stack<Character> ops = new Stack<Character>();
		Stack<Integer> vals = new Stack<Integer>();
		ops.push('#');
		
		s += "#";
		char[] t = s.toCharArray();
		int i = 0;
		while (!ops.isEmpty()) {
			if ('0' <= t[i] && t[i] <= '9') {
				int sum = 0;
				while ('0' <= t[i] && t[i] <= '9')
					sum = sum * 10 + t[i++] - '0';
				vals.push(sum);
			} else {
				if (compare(ops.peek(), t[i]) == 1) {
					int b = vals.pop();
					int a = vals.pop();
					vals.push(get(a, ops.pop(), b));
				} else if (compare(ops.peek(), t[i]) == -1) {
					ops.push(t[i]);
					i++;
				} else {
					ops.pop();
					i++;
				}
			}
		}
		
		return vals.pop();
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
			case '+': return 0;
			case '-': return 1;
			case '*': return 2;
			case '/': return 3;
			case '(': return 4;
			case ')': return 5;
			case '#': return 6;
			default : return 6;
		}
	}
	
	public int get(int a, char op, int b) {
		switch (op) {
			case '+': return a + b;
			case '-': return a - b;
			case '*': return a * b;
			default : return a / b;
		}
	}
}
