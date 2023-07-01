#include <zephyr/ztest.h>
#include <zephyr/kernel.h>

ZTEST(template, test_template)
{
    zassert_true(true, "Some test failed");
    printk("test finished!\n");
}

ZTEST_SUITE(template, NULL, NULL, NULL, NULL, NULL);
