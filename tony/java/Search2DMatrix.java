public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowLow = 0;
        int rowHigh = matrix.length - 1;
        
        while (rowLow <= rowHigh) {
            int rowMid = (rowLow + rowHigh) / 2;
            if (matrix[rowMid][0] == target) {
                return true;
            } else if (matrix[rowMid][0] > target) {
                rowHigh = rowMid - 1;
            } else {
                rowLow = rowMid + 1;
            }
        }
        
        if (rowHigh == -1)
            return false;
        
        rowLow--;
        int low = 0;
        int high = matrix[rowLow].length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (matrix[rowLow][mid] == target) {
                return true;
            } else if (matrix[rowLow][mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return false;
    }
}