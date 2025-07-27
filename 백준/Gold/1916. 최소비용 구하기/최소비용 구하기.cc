#include <iostream>
#include <vector>
#include <map>
#include <queue>
#define INF 1e9
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	int n, m;
	cin >> n >> m;

	vector<pair<int, int> > route[n + 1];
	int v[n + 1];
	fill(v, v + n + 1, 0);

	for (int i = 0; i < m; i++) {
		int f, t, c;
		cin >> f >> t >> c;

		route[f].push_back(make_pair(t, c));
	}

	int dist[n + 1];
	fill(dist, dist + n + 1, INF); // 모든 거리의 비용을 최대로 설정
	// 적은 비용을 가진 순으로 재정렬
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

	int s, e;
	cin >> s >> e;

	// 실행
	q.push(make_pair(0, s));
	dist[s] = 0;

	while (!q.empty()) {
		int cost = q.top().first;
		int curr = q.top().second;

		q.pop();

		if (!v[curr]) {
			v[curr] = 1;

			if (curr == e) continue; // 도착점이라면 패스

			for (int i = 0; i < route[curr].size(); i++) { //
				int next = route[curr][i].first; // 다음 도착할 정점의 번호
				int ncost = route[curr][i].second; // 다음 도착할 정점까지의 비용

				if (dist[next] > dist[curr] + ncost) { // 여기까지 온 거리에 다음 정점까지 비용을 더한 값이 다음 거리까지의 비용보다 적으면 갱신
					dist[next] = dist[curr] + ncost;
					q.push(make_pair(dist[next], next));
				}
			}
		}
	}

	cout << dist[e];

	return 0;
}