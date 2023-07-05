#!/bin/bash
echo "This takes a while, go grab a coffee or something..."

set -u

die()
{
    echo "$@" 1>&2
    exit 1
}

ensure_executable() { which $1 || die "Executable not found: $1" ; }

export WORKSPACE_PATH=$(pwd)
echo "WORKSPACE_PATH: $WORKSPACE_PATH"

cd "${0%/*}/.." && [ -d app ] || die "project root does not contain app directory?"

# Fetch git submodules
git config --global --add safe.directory ./zephyr
git submodule update --init --recursive || die "git submodule update failed"

# Setup Python virtual environment
cd $WORKSPACE_PATH
python3 -m venv venv || die "Failed to create Python virtual environment"
. venv/bin/activate || die "Failed to activate Python virtual environment"
pip3 install -r ./verification/integration/requirements.txt || die "Failed to install Python dependencies"

# Run west update
cd $WORKSPACE_PATH
west update || die "west update failed"

west zephyr-export || die "west zephyr-export failed"
