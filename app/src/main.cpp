#include <zephyr/kernel.h>
#include <iostream>

int main()
{
    int x;
    std::cout << "The value of x is: " << x << std::endl;

    while (true)
    {
        k_sleep(K_MSEC(1000));
    }
}
