"""
test_isadora.py

Comprehensive test suite for Isadora (ICAO 1983 ISA implementation).
Tests atmospheric properties, unit conversions, derived quantities, and constants.
"""

import os, sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import isadora
from isadora import ISA, UnitRegistry
from isadora import ISA, CONSTANTS
from isadora.units import UnitRegistry, to_user_unit

# Reference ICAO 1983 table values (sample altitudes, SI units)
ICAO_REFERENCE = {
    0: {"T": 288.15, "P": 101325.0, "rho": 1.225},
    5: {"T": 255.65, "P": 54019.0, "rho": 0.736},
    11: {"T": 216.65, "P": 22632.0, "rho": 0.364},
    20: {"T": 216.65, "P": 5474.9, "rho": 0.0889},
    32: {"T": 228.65, "P": 868.0, "rho": 0.0132},
    47: {"T": 270.65, "P": 110.9, "rho": 0.00143},
}


# ================ ICAO Compliance Tests =================


@pytest.mark.parametrize("altitude, ref", ICAO_REFERENCE.items())
def test_isa_properties_against_icao(altitude, ref):
    atm = ISA(geopotential_height=altitude)
    # Temperature check
    assert abs(atm.temperature.value - ref["T"]) < 0.5, f"T mismatch at {altitude} km"
    # Pressure check
    assert (
        abs(atm.pressure.value - ref["P"]) / ref["P"] < 0.01
    ), f"P mismatch at {altitude} km"
    # Density check
    assert (
        abs(atm.density.value - ref["rho"]) / ref["rho"] < 0.01
    ), f"rho mismatch at {altitude} km"


# ==========================================================================================================


def test_mach_number_calculation():
    atm = ISA(geopotential_height=10)
    V = 340  # m/s
    M = atm.mach_number(V)
    # Mach number should roughly equal V / speed_of_sound
    expected = V / atm.speed_of_sound.value
    assert abs(M - expected) < 1e-3


def test_dynamic_pressure():
    atm = ISA(geopotential_height=2)
    V = 100  # m/s
    q = atm.dynamic_pressure(V)
    # q = 0.5 * rho * V^2
    expected = 0.5 * atm.density.value * V**2
    assert abs(q.value - expected) / expected < 1e-6


def test_geometric_height_conversion():
    atm = ISA(geopotential_height=10)
    h_geo = atm.geometric_height
    # Geometric height must be greater than geopotential height
    assert h_geo.value > 10


def test_to_user_unit_conversion():
    UnitRegistry._locked = False
    UnitRegistry.set_unit_standard("IMPERIAL")
    T_SI = 300.0
    T_user = to_user_unit(T_SI, "TEMPERATURE")
    # Value should be converted to Celsius
    assert isinstance(T_user.value, float)


def test_constants_immutability():
    with pytest.raises(RuntimeError):
        CONSTANTS.g = 10.0  # cannot change constants


def test_constants_values():
    # Basic sanity check
    assert abs(CONSTANTS.MSL_TEMPERATURE.value - 288.15) < 1e-6
    assert abs(CONSTANTS.g.value - 9.80665) < 1e-6


def test_layer_boundaries():
    # Troposphere-stratosphere boundary (11 km)
    atm = ISA(geopotential_height=11)
    assert type(atm.atmosphere) == isadora.base.ISATroposphere


if __name__ == "__main__":
    pytest.main()
