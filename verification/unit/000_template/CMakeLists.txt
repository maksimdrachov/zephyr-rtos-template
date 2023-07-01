# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(test_template)

FILE(GLOB app_sources src/*.c src/*.h)
target_sources(app PRIVATE ${app_sources})