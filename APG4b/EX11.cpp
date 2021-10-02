#include <iostream>
#include <string>

int calc(std::string ope, int x, int y)
{
    if (ope == "+") {
        return x + y;
    }
    else if (ope == "-") {
        return x - y;
    }
    else if (ope == "*") {
        return x * y;
    }
    else if (ope == "/") {
        return x / y;
    }
    return 0;
}

int main()
{
    int N, A, eve;
    std::cin >> N >> A;
    eve = A;
    
    for (int i = 1; i <= N; i++) {
        std::string ope;
        int b;
        std::cin >> ope >> b;
        if (ope == "/" && b == 0) {
            std::cout << "error" << std::endl;
            break;
        }
        else {
            eve = calc(ope, eve, b);
            std::cout << i << ":" << eve << std::endl;
        }
    }
}
