#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

// 방문 처리
vector<int>v[100];
int visit[100];

// dfs 함수 정의
void dfs(int x){
    for(int i = 0;i < v[x].size(); i++){
        if(!visit[v[x][i]]){
            visit[v[x][i]]=1;
            dfs(v[x][i]);
        }
    }
}

int main(){
    int n, a;
    cin >> n;

    for(int i = 0;i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> a;
            if(a) v[i].push_back(j);
        }
    }
    for(int i = 0; i < n; i++) {
        memset(visit, 0, sizeof(visit));
        dfs(i);
        for(int j = 0;j < n; j++)
            cout << visit[j] << " ";
        cout << "\n";
    }
}