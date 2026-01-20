import pytest

@pytest.fixture(scope="session")
def sea_level():
    from isadora import ISA
    return ISA(geopotential_height=0)
