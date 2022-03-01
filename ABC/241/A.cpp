#include <bits/stdc++.h>
using namespace std;

int main()
{
    int A[10];
    for (int i = 0; i < 10; i++) cin >> A[i];

    int ans = A[0];
    for (int i = 2; i > 0; i--) ans = A[ans];
    cout << ans << endl;
}
