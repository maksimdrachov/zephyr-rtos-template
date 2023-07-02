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
    stdout, stderr = await proc.communicate()

    _logger.info(f"[exited with {proc.returncode}]")
    if stdout:
        _logger.info(f"[stdout]\n{stdout.decode()}")
        assert True, "Clear build directory succeeded"
    if stderr:
        _logger.info(f"[stderr]\n{stderr.decode()}")
        assert False, "Clear build directory failed"

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
    stdout, stderr = await proc.communicate()

    _logger.info(f"[exited with {proc.returncode}]")
    if stdout:
        _logger.info(f"[stdout]\n{stdout.decode()}")
        assert True, "Build succeeded"
    if stderr:
        _logger.info(f"[stderr]\n{stderr.decode()}")
        assert False, "Build failed"

    # Flash the board
    _logger.info("Flashing the board")
    proc = await asyncio.create_subprocess_exec(
        "west",
        "flash",
        cwd=PROJECT_DIR,
    )
    stdout, stderr = await proc.communicate()

    _logger.info(f"==============================")
    _logger.info(f"[exited with {proc.returncode}]")
    _logger.info(f"==============================")

    assert False
    if stdout:
        _logger.info(f"[stdout]\n{stdout.decode()}")
        assert True, "Flash succeeded"
    if stderr:
        _logger.info(f"[stderr]\n{stderr.decode()}")
        assert False, "Flash failed"
