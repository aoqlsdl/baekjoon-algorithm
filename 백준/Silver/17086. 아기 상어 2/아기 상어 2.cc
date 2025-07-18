#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	// 입력
	int n, m;
	cin >> n >> m;

	vector<vector<int>> sea(n, vector<int>(m));
	vector<vector<int>> v(n, vector<int>(m, 0));
	vector<pair<int, int>> bs;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> sea[i][j];
			if (sea[i][j] == 1) bs.push_back({i, j});
		}
	}

	queue <pair<int, int>> q;

	// 아기상어 위치를 큐에 추가하고 방문 처리
	for (auto p : bs) {
		q.push(p);
		v[p.first][p.second] = 1;
	}

	int dx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
	int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

	// bfs를 이용한 최단거리 측정
	while (!q.empty()) {
		auto [x, y] = q.front(); q.pop();

		// 대각선을 포함해 순회
		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			// 범위 안에 있고 방문하지 않았다면
			if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
				if (v[nx][ny] == 0) {
					v[nx][ny] = v[x][y] + 1;
					q.push({nx, ny});
				}
			}
		}
	}

	int res = 0;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < m; j++) res = max(res, v[i][j]);
	
	
	cout << res - 1;
	return 0;
}