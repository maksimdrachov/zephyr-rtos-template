import asyncio
import pytest
import logging
from pathlib import Path

pytestmark = pytest.mark.asyncio

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent.parent

_logger = logging.getLogger(__name__)


async def test_blinky() -> None:
    """
    All this test does is make sure we are able to flash the blinky sample successfully.
    """

    _logger.info("PROJECT_DIR: %s", PROJECT_DIR)

    # Clear the build directory
    _logger.info("Clearing the build directory")
    proc = await asyncio.create_subprocess_exec(
        "rm",
        "-rf",
        "build",
        cwd=PROJECT_DIR,
    )
    await proc.communicate()
    assert proc.returncode == 0, "Failed to clear build directory"

    # Build the board
    _logger.info("Building the board")
    proc = await asyncio.create_subprocess_exec(
        "west",
        "build",
        "-b",
        "nucleo_l432kc",
        "./zephyr/samples/basic/blinky",
        cwd=PROJECT_DIR,
    )
    await proc.communicate()
    assert proc.returncode == 0, "Build failed"

    # Flash the board
    _logger.info("Flashing the board")
    proc = await asyncio.create_subprocess_exec(
        "west",
        "flash",
        cwd=PROJECT_DIR,
    )
    await proc.communicate()
    assert proc.returncode == 0, "Flash failed"
