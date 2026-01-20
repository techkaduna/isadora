import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="session")
def sea_level():
    from isadora import ISA

    return ISA(geopotential_height=0)
