import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isadora import ISA

def test_speed_of_sound_sea_level():
    """
    Speed of sound at sea level ≈ 340.3 m/s
    """
    atm = ISA(geopotential_height=0)
    assert abs(atm.speed_of_sound.value - 340.3) < 0.5


def test_ideal_gas_identity():
    """
    Validate rho = P / (R * T)
    """
    atm = ISA(geopotential_height=8)

    rho_calc = atm.pressure.value / (287.052874 * atm.temperature.value)
    rho_model = atm.density.value

    assert abs(rho_calc - rho_model) / rho_model < 1e-6
