#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	int dp[10001]; // 0으로 채워진 상태
	
	dp[1] = 1; dp[2] = 3;
	
	// dp[n] = dp[n - 2] * 2 + dp[n - 1]
	int i;
	for (i=3; i <= n; i++)  {
		if (dp[i] == 0) {
			dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007;
		}
	}

	cout << dp[n];

	return 0;
}