#include <iostream>
using namespace std;

/**
 * 의사코드
 * 1. vector<pair> 형식으로 입력을 받아 {분자, 분모}로 인자를 구성한다.
 * 2. 분자, 분모에 동일한 수를 곱해준다.
 * 3. 분자끼지 더해 합을 구하고, 변수 a에 저장한다.
 * 4. 분모를 변수 b에 저장한다.
 * 5-1. a % b != 0이면 a / b
 * 5-2. a % b == 0이면 현재 a, b를 순서대로 출력한다.
 */

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	int a, b, c, d;
    cin >> a >> b;
    cin >> c >> d;

    // 통분, 합 구하기
    int n1 = a * d + c * b;
    int n2 = b * d;

    // 기약분수로 만들기
    int g = gcd(n1, n2);
    n1 /= g;
    n2 /= g;

    cout << n1 << " " << n2;

	return 0;
}