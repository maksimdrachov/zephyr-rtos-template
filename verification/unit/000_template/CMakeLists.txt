# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

# This sets common build options for all targets.
set(ZephyrBuildConfiguration_ROOT ${CMAKE_CURRENT_LIST_DIR}/../cmake/modules)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/../cmake/modules)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(test_template)

FILE(GLOB app_sources src/*.cpp src/*.hpp)
target_sources(app PRIVATE ${app_sources})

# Setup Clang-Tidy
set_target_properties(
        app PROPERTIES
        INTERPROCEDURAL_OPTIMIZATION TRUE
        CMAKE_C_CLANG_TIDY "${clang_tidy}"
        CMAKE_CXX_CLANG_TIDY "${clang_tidy}"
)

