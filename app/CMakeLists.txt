# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

# This sets common build options for all targets.
set(ZephyrBuildConfiguration_ROOT ${CMAKE_CURRENT_LIST_DIR}/../cmake/modules)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/../cmake/modules)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(blinky)

# target_sources(app PRIVATE src/main.c)
target_sources(app PRIVATE src/main.cpp)
target_include_directories(app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src)

# Setup Clang-Tidy
set_target_properties(
        app PROPERTIES
        INTERPROCEDURAL_OPTIMIZATION TRUE
        CMAKE_C_CLANG_TIDY "${clang_tidy}"
        CMAKE_CXX_CLANG_TIDY "${clang_tidy}"
)
