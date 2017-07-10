class Solution {
public:
    double findKth(vector<int>::iterator a, int m, vector<int>::iterator b, int n, int k) {
        if (m > n)
            findKth(b, n, a, m, k);
        if (m == 0)
            return b[k - 1];
        if (k == 1)
            return min(a[0], b[0]);
        int pa = min(k / 2, m), pb = k - pa;
        if (a[pa - 1] < b[pb - 1]) {
            return findKth(a + pa, m - pa, b, n, k - pa);
        } else if (a[pa - 1] > b[pb - 1]) {
            return findKth(a, m, b + pb, n - pb, k - pb);
        } else {
            return a[pa - 1];
        }
    }
    
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        if (total % 2 != 0) {
            return findKth(nums1.begin(), m, nums2.begin(), n, total / 2 + 1);
        } else {
            return (findKth(nums1.begin(), m, nums2.begin(), n, total / 2) +
                    findKth(nums1.begin(), m, nums2.begin(), n, total / 2 + 1)) / 2.0;
        }    
    }
};