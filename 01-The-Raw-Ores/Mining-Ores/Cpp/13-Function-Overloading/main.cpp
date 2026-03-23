#include <iostream>

int main () {
    auto result = ( 10 <=>  20) > 0; //Spaceship operator to check complier support
    std::cout << result << std::endl;
}