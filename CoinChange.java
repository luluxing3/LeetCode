public class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] d = new int[amount + 1];
        for (int i = 0; i < amount+1; i++)
            d[i] = amount + 1;
        d[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (i >= coins[j] && d[i - coins[j]] + 1 < d[i])
                    d[i] = d[i - coins[j]] + 1;
            }
        }
        return d[amount] > amount ? -1 : d[amount];
    }
}