"""
isadora.constants
=================

Physical and atmospheric constants used throughout the ISADORA package.

This module defines a centralized container for physical constants
required by the International Standard Atmosphere (ISA) model and
related thermodynamic computations. All constants are expressed in
SI units and wrapped using the internal unit-handling system.

The constants are instantiated once and exposed through the
:data:`CONSTANTS` object.

Notes
-----
- Constants are stored as unit-aware objects where applicable.
- Values correspond to standard ISA sea-level conditions unless
  otherwise stated.
- This module is intended to be read-only after initialization.

Classes
-------
__Constants

Attributes
----------
CONSTANTS : __Constants
    Singleton instance containing all defined constants.
"""

from .units import _UnitParam


class __Constants:
    """
    Container class for physical and atmospheric constants.

    This class encapsulates all constants used by the ISA model,
    including sea-level reference values and universal physical
    constants. Each constant is defined as a unit-aware parameter
    and initialized with its corresponding numerical value.

    Notes
    -----
    This class is intended for internal use only and should not be
    instantiated directly by users. A singleton instance is exposed
    as :data:`CONSTANTS`.
    """

    MSL_TEMPERATURE: _UnitParam = _UnitParam("MSL_TEMPERATURE", "TEMPERATURE")
    MSL_PRESSURE: _UnitParam = _UnitParam("MSL_PRESSURE", "PRESSURE")
    MSL_DENSITY: _UnitParam = _UnitParam("MSL_DENSITY", "DENSITY")
    MSL_DYNAMIC_VISCOSITY: _UnitParam = _UnitParam(
        "MSL_DYNAMIC_VISCOSITY", "DYNAMIC_VISCOSITY"
    )
    MSL_KINEMATIC_VISCOSITY: _UnitParam = _UnitParam(
        "MSL_KINEMATIC_VISCOSITY", "KINEMATIC_VISCOSITY"
    )

    g: _UnitParam = _UnitParam("g", "SPEED")
    R: _UnitParam = _UnitParam("R", "SPEC_HEAT_CONSTANT")
    R_: _UnitParam = _UnitParam("R_", "UNIV_GAS_CONSTANT")
    r: _UnitParam = _UnitParam("r", "DISTANCE")
    M: _UnitParam = _UnitParam("M", "EARTH_MOLAR_MASS")
    a_o: _UnitParam = _UnitParam("a_o", "SPEED")

    y: float | int = 1.4

    c_p: _UnitParam = _UnitParam("c_p", "SPEC_HEAT_CONSTANT")
    c_v: _UnitParam = _UnitParam("c_v", "SPEC_HEAT_CONSTANT")
    S: _UnitParam = _UnitParam("S", "TEMPERATURE")

    def __init__(self):
        """
        Initialize all physical constants.

        All constants are assigned their standard ISA values and
        converted into unit-aware objects.
        """

        self.MSL_TEMPERATURE = 288.15
        """Sea-level standard temperature.

        Notes
        -----
        Value is defined according to ISA.

        Unit
        ----
        Kelvin (K)
        """

        self.MSL_PRESSURE = 101325.0
        """Sea-level standard pressure.

        Unit
        ----
        Pascal (Pa)
        """

        self.MSL_DENSITY = 1.2250122659907
        """Sea-level standard air density.

        Unit
        ----
        kg/m³
        """

        self.MSL_DYNAMIC_VISCOSITY = 1.7894e-5
        """Sea-level dynamic viscosity of air.

        Unit
        ----
        kg/(m·s)
        """

        self.g = 9.80665
        """Standard acceleration due to gravity.

        Unit
        ----
        m/s²
        """

        self.R = 287.052874
        """Specific gas constant for dry air.

        Unit
        ----
        J/(kg·K)
        """

        self.R_ = 8.314462618
        """Universal gas constant.

        Unit
        ----
        J/(mol·K)
        """

        self.r = 6371.0
        """Mean radius of the Earth.

        Notes
        -----
        Used in geopotential altitude calculations.

        Unit
        ----
        km
        """

        self.M = 0.0289644
        """Molar mass of dry air under ISA conditions.

        Unit
        ----
        kg/mol
        """

        self.y = 1.4
        """Ratio of specific heats (gamma).

        Notes
        -----
        Dimensionless.
        """

        self.c_p = 1005.0
        """Specific heat at constant pressure.

        Unit
        ----
        J/(kg·K)
        """

        self.c_v = 718.0
        """Specific heat at constant volume.

        Unit
        ----
        J/(kg·K)
        """

        self.S = 110.4
        """Sutherland's constant.

        Unit
        ----
        Kelvin (K)
        """

        self.MSL_KINEMATIC_VISCOSITY = (
            self.MSL_DYNAMIC_VISCOSITY / self.MSL_DENSITY
        ).value
        """Sea-level kinematic viscosity.

        Unit
        ----
        m²/s
        """

        self.a_o = ((self.y * self.R * self.MSL_TEMPERATURE) ** 0.5).value
        """Speed of sound at sea level.

        Unit
        ----
        m/s
        """


CONSTANTS = __Constants()
"""
Singleton instance containing all physical and atmospheric constants.

This object should be imported and used wherever constants are
required within the ISADORA package.
"""
