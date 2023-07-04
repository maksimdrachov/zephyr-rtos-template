get_filename_component(WORKSPACE_DIR
                       ${CMAKE_CURRENT_LIST_DIR}/../..
                       ABSOLUTE
)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_EXTENSIONS 0)
set(CMAKE_CXX_EXTENSIONS 0)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} \
    -Wall -Wextra -Werror -Wdouble-promotion -Wswitch-enum -Wfloat-equal -Wundef -Wconversion \
    -Wtype-limits -Wsign-conversion -Wcast-align -Wmissing-declarations -Wframe-larger-than=1024 \
    -fno-strict-aliasing -fno-strict-overflow \
    -fno-math-errno -fno-signed-zeros -fno-trapping-math -fassociative-math -freciprocal-math \
    -O1")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} \
    -Wall -Wextra -Werror -Wdouble-promotion -Wswitch-enum -Wfloat-equal -Wundef -Wconversion \
    -Wtype-limits -Wsign-conversion -Wcast-align -Wmissing-declarations -Wframe-larger-than=1024 \
    -Wzero-as-null-pointer-constant -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -Wold-style-cast \
    -fno-strict-aliasing -fno-strict-overflow \
    -fno-math-errno -fno-signed-zeros -fno-trapping-math -fassociative-math -freciprocal-math \
    -O1")

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} \
    -Wall -Wextra -Werror -Wdouble-promotion -Wswitch-enum -Wfloat-equal -Wundef -Wconversion \
    -Wtype-limits -Wsign-conversion -Wcast-align -Wmissing-declarations -Wframe-larger-than=1024 \
    -Wzero-as-null-pointer-constant -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -Wold-style-cast \
    -fno-strict-aliasing -fno-strict-overflow \
    -fno-math-errno -fno-signed-zeros -fno-trapping-math -fassociative-math -freciprocal-math \
    -O1")

# Configure clang-tidy via wrapper. Clang-tidy may use separate config files .clang-tidy per directory.
# The wrapper removes cross-arch-specific flags like -march that clang-tidy would normally trip on.
# We may need to further modify flags to make clang-tidy accept the code for our target architecture.
# Overwrite the cache to disable Clang-Tidy checks for faster compilation.
set(clang_tidy ${WORKSPACE_DIR}/scripts/clang_tidy_wrapper.py CACHE STRING "Clang-Tidy executable path")
message(STATUS "clang_tidy: ${clang_tidy}")

# Configure clang-format
find_program(clang_format NAMES clang-format)
if (NOT clang_format)
    message(WARNING "Could not locate clang-format; autoformatting is not possible")
else()
    file(
        GLOB_RECURSE format_files
        ${WORKSPACE_DIR}/app/src/*.[ch]
        ${WORKSPACE_DIR}/app/src/*.[ch]pp
        ${WORKSPACE_DIR}/verification/unit/*/*.[ch]
        ${WORKSPACE_DIR}/verification/unit/*/*.[ch]pp
    )
    message(STATUS "Using clang-format: ${clang_format}")
    add_custom_target(format COMMAND ${clang_format} -i -fallback-style=none -style=file --verbose ${format_files})
    add_custom_target(check_format COMMAND ${clang_format} -i -fallback-style=none -style=file --verbose --dry-run --Werror ${format_files})
endif()
