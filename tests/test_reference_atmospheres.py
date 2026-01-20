import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isadora import ISA

# ============================================================================
# ICAO 1983 reference values (geopotential altitude, km)
# ============================================================================

ICAO_TABLE = {
    5: {"T": 255.65, "P": 54019.9, "rho": 0.73612},
    16: {"T": 216.65, "P": 10287.5, "rho": 0.16542},
    25: {"T": 221.65, "P": 2511.02, "rho": 0.03947},
    40: {"T": 251.05, "P": 277.52, "rho": 0.00385},
}

TOLERANCES = {
    "T_abs": 0.2,  # K
    "P_rel": 0.003,  # 0.3 %
    "rho_rel": 0.005,  # 0.5 %
}


def relative_error(reference, actual):
    return abs(actual - reference) / reference


@pytest.mark.parametrize("alt_km,ref", ICAO_TABLE.items())
def test_isa_against_icao(alt_km, ref):
    """
    Validate ISA against ICAO 1983 reference atmosphere.
    """
    atm = ISA(geopotential_height=alt_km)

    T = atm.temperature.value
    P = atm.pressure.value
    rho = atm.density.value

    assert abs(T - ref["T"]) <= TOLERANCES["T_abs"]
    assert relative_error(ref["P"], P) <= TOLERANCES["P_rel"]
    assert relative_error(ref["rho"], rho) <= TOLERANCES["rho_rel"]
