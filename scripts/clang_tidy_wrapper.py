#!/usr/bin/env python
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
# This wrapper is needed for invoking clang-tidy from within CMake-based build system.
# CMake passes all compiler options directly to clang-tidy as-is, which doesn't work during cross-compilation
# because clang-tidy doesn't understand cross-compiler's options and bails out with an error.
# It is not possible to make clang-tidy ignore unrecognized arguments, so we use this wrapper to remove them.

import os, re, sys

DENY = [
    re.compile(r"-march.*"),
    re.compile(r"-mcpu.*"),
    re.compile(r"-mthumb.*"),
    re.compile(r"-mfloat.*"),
    re.compile(r"-mno-thumb.*"),
    re.compile(r"-fno-builtin"),
    re.compile(r"-fno-fat-lto-objects"),
    re.compile(r"-fconserve-stack"),
    re.compile(r"-f.*-sections"),
    re.compile(r"-f.*-cxa-"),
    re.compile(r"-fno-printf-return-value"),
    re.compile(r"-fno-reorder-functions"),
    re.compile(r"-mfp16-format=ieee"),
    re.compile(r"-fno-defer-pop"),
    re.compile(r"--param=min-pagesize=0"),
    re.compile(r"--specs=picolibc.specs")
]

args = list(
    filter(
        lambda ar: not any(x.match(ar) for x in DENY),
        sys.argv[1:],
    )
)
print(f"{sys.argv[0]}", args, file=sys.stderr)

os.sync()  # exec() does not flush before replacing the current process, so we have to do it manually.
sys.stdout.flush()
sys.stderr.flush()
os.execvp("clang-tidy", args)
sys.exit(1)  # exec() does not return on success, so if we reach here, it's an error.
