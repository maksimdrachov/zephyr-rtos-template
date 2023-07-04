#include <memory>  // for std::unique_ptr
#include <zephyr/ztest.h>

struct cpp_fixture
{
    int x;
};

ZTEST_SUITE(cpp, NULL, NULL, NULL, NULL, NULL);

ZTEST_F(cpp, test_fixture_created_and_initialized)
{
    std::unique_ptr<cpp_fixture> unique_cpp_struct(new cpp_fixture);
    unique_cpp_struct->x = 5;
    zassert_equal(5, unique_cpp_struct->x);
}
