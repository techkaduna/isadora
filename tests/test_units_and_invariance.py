import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isadora import ISA


def test_geometric_vs_geopotential_height():
    """
    ISA results should be invariant under
    geometric vs geopotential height conversion.
    """
    atm_geo = ISA(geopotential_height=10)
    atm_geom = ISA.from_geometric_height(geometric_height=10000)

    assert abs(atm_geo.pressure.value - atm_geom.pressure.value) < 1.0
    assert abs(atm_geo.temperature.value - atm_geom.temperature.value) < 0.05
