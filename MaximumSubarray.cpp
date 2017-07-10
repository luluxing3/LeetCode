//
//  MaximumSubarray.cpp
//  DynamicProgramming
//
//  Created by Tony Hu on 2017/7/10.
//  Copyright © 2017年 Tony Hu. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int maxSubArray(vector<int> &nums) {
    int result = INT_MIN, sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (sum > result)
            result = sum;
        if (sum > 0)
            sum += nums[i];
        else
            sum = nums[i];
    }
    return result;
}

int main() {
    int a[] = {-2,1,-3,4,-1,2,1,-5,4};
    //int a[] = {-2,1,-3,-1,2,1,-5};
    vector<int> nums(a, a + 9);
    
    cout << maxSubArray(nums) << endl;
    
    return 0;
}