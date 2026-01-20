import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isadora import ISA


def test_hydrostatic_balance():
    """
    Verify hydrostatic equilibrium:
    dP/dh ≈ -rho * g
    """
    dh = 0.01  # km

    atm1 = ISA(geopotential_height=10.0)
    atm2 = ISA(geopotential_height=10.0 + dh)

    dP = atm2.pressure.value - atm1.pressure.value
    avg_rho = 0.5 * (atm1.density.value + atm2.density.value)

    lhs = dP / (dh * 1000.0)
    rhs = -avg_rho * 9.80665

    assert abs(lhs - rhs) / abs(rhs) < 0.01


def test_pressure_monotonicity():
    """
    Pressure must decrease monotonically with altitude.
    """
    previous = None

    for h in range(0, 45):
        atm = ISA(geopotential_height=h)
        if previous is not None:
            assert atm.pressure.value < previous
        previous = atm.pressure.value
