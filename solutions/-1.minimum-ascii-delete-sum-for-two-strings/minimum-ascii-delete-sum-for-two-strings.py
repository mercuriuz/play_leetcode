class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int sz1, sz2;
        sz1 = s1.length();
        sz2 = s2.length();
        int dp[sz1+1][sz2+1];
        memset(dp, 0, sizeof(dp));   
        for (int i = sz1-1; i >= 0; i--)
            dp[i][sz2] += dp[i+1][sz2] + (int)s1[i];
        for (int j = sz2-1; j >= 0; j--)
            dp[sz1][j] += dp[sz1][j+1] + (int)s2[j];
        for (int i = sz1-1; i >= 0; i--) {
            for (int j = sz2-1; j >= 0; j--) {
                if (s1[i] == s2[j])
                    dp[i][j] = dp[i+1][j+1];
                else {
                    int a = dp[i+1][j] + (int)s1[i];
                    int b = dp[i][j+1] + (int)s2[j];
                    dp[i][j] = a < b ? a : b;
                }
            }
        }
        return dp[0][0];
    }
};