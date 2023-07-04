#include <zephyr/kernel.h>

int main()
{
    while (true)
    {
        k_sleep(K_MSEC(1000));
    }
}
