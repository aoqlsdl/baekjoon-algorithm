#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int> > arr;

    for (int i = 0; i < n; i++)
    {
        int start, end;
        cin >> end >> start;
        arr.push_back(make_pair(start, end));
    }
    sort(arr.begin(), arr.end());

    int t = arr[0].first;
    int ans = 1;
    int j = 0;
    for (int i = 1; i <= n; i++)
    {
        if (arr[i].second >= t)
        {
            ans++;
            t = arr[i].first;
        }
    }
    cout << ans;
}