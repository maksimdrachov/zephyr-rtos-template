#!/bin/bash

die()
{
    echo "$@" 1>&2
    exit 1
}

# Array of paths containing unit tests
test_paths=(
  "./verification/unit/000_template"
  # Add more paths as needed
)

# save workspace path
workspace_path=$(pwd)

# Activate Python virtual environment
. venv/bin/activate || die "Failed to activate Python virtual environment"

# Build and execute each unit test
for path in "${test_paths[@]}"
do
  echo "Building and executing test in $path..."

  # clear previous build/logs
  rm -rf build

  west build -b nucleo_l432kc $path || die "Build failed"

  sleep 4s

  # run the test
  ./zephyr/scripts/twister --device-testing --device-serial /dev/serial/by-id/usb-STMicroelectronics_STM32_STLink_0675FF545071494867194046-if02 -p nucleo_l432kc -T $path

  echo "Test in $path executed."

  if grep -q "PROJECT EXECUTION FAILED" ./twister-out/twister.log; then
    echo "======Unit test failed======"
    echo "failed on: $path"
    exit 1
  elif grep -q "PROJECT EXECUTION SUCCESSFUL" ./twister-out/twister.log; then
    echo "======Unit test passed======"
  else
    echo "======./twister-out/twister.log not found?======"
    echo "failed on: $path"
    exit 2
  fi

  cd "$workspace_path"
done

echo "All unit tests passed:"
for path in "${test_paths[@]}"
do
  echo "$path"
done

exit 0
