#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
    long long n, k;
    cin >> n >> k;
    vector<long long> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h.at(i);
    }

    while (!h.empty() && k > 0) {
        vector<long long>::iterator iter = max_element(h.begin(), h.end());
        size_t index = distance(h.begin(), iter);
        h.erase(h.begin() + index);
        k--;
    }

    cout << accumulate(h.begin(), h.end(), 0) << endl;
}
