#include<iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int arr[10] = {0};
	int n;
	cin >> n;

	while (n > 0) {
		if (n % 10 == 6 || n % 10 == 9) {
			if (arr[6] == arr[9]) arr[6]++;
			else arr[9]++;
		}
		else arr[n % 10]++;

		n /= 10;
	}

	int max = arr[0];
	for (int i = 1; i < 10; i++) {
		if (max < arr[i]) max = arr[i];
	}

	cout << max;

	return 0;
}