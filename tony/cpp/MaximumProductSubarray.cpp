class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int result = INT_MIN;
        int m = 1, n = 1; // 考虑正负号的情况
        int tmp_max, tmp_min;
        for (int i = 0; i < nums.size(); ++i) {
            tmp_max = max(m * nums[i], n * nums[i]);
            tmp_min = min(m * nums[i], n * nums[i]);
            m = max(tmp_max, nums[i]);
            n = min(tmp_min, nums[i]);
            result = max(result, m);
        }
        return result;
    }
};