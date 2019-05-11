#include<iostream>
#include<algorithm>
using namespace std;
static const int MAX = 200000;

// O(n^2)になるアルゴリズム
int main() {
    int R[MAX], n;

    cin >> n;
    for ( int i = 0; i < n ; i++ ) cin >> R[i];

    int maxv = -2000000000;
    int minv = R[0];

    for (int j = 1; j < n -1; j++) {
	for (int i = 0; i < j - 1; i++ ) {
	    maxv = max(maxv, R[j]-R[i]);
	}
    }

    cout << maxv << endl;

    return 0;
}
