#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

int main()
{
    int n, k;
    std::cin >> n >> k;
    k -= 1;
    std::vector<int> p(n);
    for (int &x: p) {
        int a, b, c;
        std::cin >> a >> b >> c;
        x = a + b + c;
    }

    std::vector<int> q = p;
    
    std::nth_element(begin(q), begin(q) + k, end(q), std::greater<>());
    for (int x: p) {
        std::cout << (x + 300 >= q[k] ? "Yes" : "No") << std::endl;
    }
}
