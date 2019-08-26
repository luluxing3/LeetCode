//
//  main.cpp
//  DynamicProgramming
//
//  Created by Tony Hu on 2017/7/9.
//  Copyright © 2017年 Tony Hu. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// recursive solution
int minTotal(vector<vector<int>> &triangle, int i, int j) {
    if (i == triangle.size())
        return triangle[i][j];
    int x = minTotal(triangle, i + 1, j);
    int y = minTotal(triangle, i + 1, j + 1);
    
    return max(x, y) + triangle[i][j];
}

// 记忆性递归，保存中间结果，避免重复计算
int minTotal(vector<vector<int>> &triangle, vector<vector<int>> &minSum, int i, int j) {
    if (minSum[i][j] != -1)
        return minSum[i][j];
    if (i == triangle.size()) {
        minSum[i][j] = triangle[i][j];
    } else {
        int x = minTotal(triangle, minSum, i + 1, j);
        int y = minTotal(triangle, minSum, i + 1, j + 1);
        minSum[i][j] = min(x, y) + triangle[i][j];
    }
    
    return minSum[i][j];
}

// 非递归方法 这里minSum可以直接在原triangle操作
int minTotal(vector<vector<int>> &triangle, vector<vector<int>> &minSum) {
    int n = triangle.size();
    for (int i = 0; i < n; ++i)
        minSum[n][i] = triangle[n][i];
    for (int i = n - 2; i >= 0; --i)
        for (int j = 0; j <= i; ++j)
            minSum[i][j] = min(minSum[i + 1][j], minSum[i + 1][j + 1]) + triangle[i][j];
    return minSum[0][0];
}

// 优化过的非递归方法
int minTotal(vector<vector<int>> &triangle) {
    int n = triangle.size();
    int d[n]; // 只用一维数组
    for (int i = 0; i < n; ++i)
        d[i] = triangle[n - 1][i];
    for (int i = n - 2; i >= 0; ++i)
        for (int j = 0; j <= i; ++j) {
            d[j] = min(d[j], d[j + 1]) + triangle[i][j];
        }
    return d[0];
}


int main(int argc, const char * argv[]) {
    vector<vector<int>> triangle;
    // int n;
    // cin >> n;
    // for (int i = 0; i < n; ++i)
    //     for (int j = 0; j <= i; ++j)
    //         cin >> triangle[i][j];
    // cout << minTotal(triangle) << endl;
    
    return 0;
}
