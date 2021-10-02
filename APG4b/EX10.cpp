#include <iostream>
#include <string>

int main()
{
    int A, B;
    std::cin >> A >> B;

    std::string a = std::string(A, ']');
    std::string b = std::string(B, ']');
    std::cout << "A:" << a << std::endl;
    std::cout << "B:" << b << std::endl;
}
