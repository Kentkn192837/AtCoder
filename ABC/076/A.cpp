#include <iostream>

int main()
{
    int R, G;
    std::cin >> R >> G;

    long long b = 2 * G - R;
    std::cout << b << std::endl;
}
