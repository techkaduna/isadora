"""
examples.py
===========

Example usage script for the ISADORA International Standard Atmosphere (ISA) model.

This script demonstrates how to instantiate the :class:`isadora.ISA` class
at various geopotential altitudes and query common atmospheric properties,
including temperature, pressure, density, viscosities, and derived quantities
such as Mach number and speed of sound.

The examples cover multiple atmospheric layers:
- Troposphere
- Tropopause
- Stratosphere (lower and upper regions)

Notes
-----
- All calculations are internally performed in SI units.
- Output units depend on the active unit standard defined in
  :mod:`isadora.units.UnitRegistry`.
- This script modifies ``sys.path`` to allow execution directly from the
  repository without installing the package.

This file is intended for demonstration, testing, and quick inspection
of model behavior. It is **not** part of the public API.

Examples
--------
Run the script from the project root::

    python examples/examples.py

You should see printed atmospheric properties for several altitudes.
"""

import os
import sys

# Allow running this script directly without installing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from isadora import ISA


def _print_atmosphere_state(atm: ISA):
    """
    Print a summary of atmospheric properties for a given ISA instance.

    Parameters
    ----------
    atm : ISA
        An initialized ISA atmosphere object.
    """
    print(atm)
    print("temperature", atm.temperature)
    print("pressure", atm.pressure)
    print("density", atm.density)
    print("dynamic_viscosity", atm.dynamic_viscosity)
    print("kinematic_viscosity", atm.kinematic_viscosity)
    print("temperature_ratio", atm.temperature_ratio)
    print("density_ratio", atm.density_ratio)
    print("pressure_ratio", atm.pressure_ratio)
    print("speed_of_sound", atm.speed_of_sound)
    print("mach_number(20)", atm.mach_number(20))
    print("dynamic_pressure(25)", atm.density_ratio)
    print("geometric_height", atm.geometric_height)


# ============================================================================
# Troposphere example (≈ 5 km)
# ============================================================================
atm = ISA(geopotential_height=5)
_print_atmosphere_state(atm)

print("=" * 80)

# ============================================================================
# Upper troposphere / lower tropopause example (≈ 15 km)
# ============================================================================
atm = ISA(geopotential_height=15)
_print_atmosphere_state(atm)

print("=" * 80)

# ============================================================================
# Tropopause / lower stratosphere example (≈ 25 km)
# ============================================================================
atm = ISA(geopotential_height=25)
_print_atmosphere_state(atm)

print("=" * 80)

# ============================================================================
# Upper stratosphere example (≈ 45 km)
# ============================================================================
atm = ISA(geopotential_height=45)
_print_atmosphere_state(atm)
