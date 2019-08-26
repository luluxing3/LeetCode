public class Solution {
    public double myPow(double x, int n) {
        if (n == 0)
            return 1;
        if (n < 0 && n == Integer.MIN_VALUE) {
            return 1.0 / (myPow(x, Integer.MAX_VALUE) * x);
        } else if (n < 0 && n != Integer.MIN_VALUE) {
            return 1.0 / myPow(x, -n);
        }
        
        double num = myPow(x, n>>1);
        if (n % 2 == 0) {
            return num * num;
        } else {
            return num * num * x;
        }
    }
}