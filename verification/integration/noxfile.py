# Use "nox -s NAME" to run a specific session NAME.
# More info at https://nox.thea.codes/en/stable/usage.html

import os
import shutil
from pathlib import Path
from tempfile import mkdtemp
import nox

# REQUIRED_COVERAGE_PCT = 80

ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "tests"
VERIFICATION_ROOT = ROOT_DIR.parent
PROJECT_ROOT = VERIFICATION_ROOT.parent


@nox.session(python=False)
def clean(session):
    wildcards = [
        "dist",
        "build",
        "htmlcov",
        ".coverage*",
        ".*cache",
        ".*compiled",
        "*.egg-info",
        "*.log",
        "*.tmp",
        ".nox",
    ]
    for w in wildcards:
        for f in Path.cwd().glob(w):
            session.log(f"Removing: {f}")
            shutil.rmtree(f, ignore_errors=True)


@nox.session(reuse_venv=True)
def test(session):
    session.install("-r", "requirements.txt")

    pytest_env = {
        "PATH": session.env["PATH"],
    }
    session.log(f"Environment: {pytest_env}")
    session.run("coverage", "run", "-m", "pytest", *session.posargs, env=pytest_env)
