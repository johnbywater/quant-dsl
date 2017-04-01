#!/usr/bin/env python
import os
import subprocess
import sys


def build_and_release(cwd):
    # Build and upload to PyPI.
    subprocess.check_call([sys.executable, 'setup.py', 'sdist', 'upload', '-r', 'pypi'], cwd=cwd)


if __name__ == '__main__':
    cwd = os.path.join(os.environ['HOME'], 'PyCharmProjects', 'quantdsl')
    build_and_release(cwd)
