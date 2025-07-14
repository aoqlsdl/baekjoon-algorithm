#include <iostream>
#include <algorithm>
using namespace std;

int t, m, n, k, x, y, ans;
int field[50][50];
// 남 북 서 동
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

// dfs 탐색
void dfs(int x, int y) {
	// 방문 처리
	field[x][y] = 0;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		
		if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
		if (field[nx][ny] == 1) {
			dfs(nx, ny);
		}
	}
}

int main() {
	cin >> t;

	for (int q = 0; q < t; q++) {
		// 입력
		cin >> m >> n >> k;

		for (int i = 0; i < k; i++) {
			cin >> x >> y;
			field[x][y] = 1;
		}

		// 배추밭 dfs 탐색
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (field[i][j] == 1) {
					dfs(i, j);
					ans++;
				}
			}
		}

		// 마리 수 출력 후 배열 및 정답 초기화
		cout << ans << '\n';
		
		ans = 0;
		for (int i = 0; i < m; i++) {
			fill(field[i], field[i] + n, 0);
		}
	}
}