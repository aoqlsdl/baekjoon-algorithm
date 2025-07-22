#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

/**
 * 의사코드
 * 1. 암호화된 수를 string으로 받는다.
 * 2. n번째 자릿수일때 해석 가짓수 = (n - 1)번째 자릿수일 때 해석 가짓수 + (마지막 두자릿수가 26이하일 경우에만) (n - 2)번째 자릿수일 때 해석 가짓수
 */
int main() {
	// 입력
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string code; cin >> code;
	int n = code.size();

	// dp 테이블 세팅
	vector<long long> dp(n + 1);
	dp[0] = 1;

	if (code[0] == '0') dp[1] = 0;
	else dp[1] = 1;

	for (int i = 2; i <= n; i++) {
		char c1 = code[i - 2];
		char c2 = code[i - 1];

		if (c2 != '0') dp[i] += dp[i - 1];

		int num = (c1 - '0') * 10 + (c2 - '0');

		if (num >= 10 && num <= 26) dp[i] += dp[i - 2];
		
		// 버퍼 오버플로우 방지
		dp[i] %= 1000000;
	}

	cout << dp[n];

	return 0;
}