"""
isadora.base
============

Base atmospheric models for the ISADORA package.

This module implements the International Standard Atmosphere (ISA)
up to the stratosphere. It provides abstractions for atmospheric
layers and a high-level :class:`ISA` interface to compute atmospheric
properties such as temperature, pressure, density, viscosity,
speed of sound, Mach number, and dynamic pressure as a function
of altitude.

All internal computations are performed in SI units, while user-facing
values are converted back to the active user-defined unit system.

Notes
-----
- Valid only for altitudes from sea level up to the stratosphere
  (~47 km geopotential height).
- Supports both geometric and geopotential altitudes.

Classes
-------
AtmosphericLayer
IsothermalLayer
ISATroposphere
ISATropopause
ISAStratosphere
ISA

Functions
---------
_choose_atmosphere
"""

import math
from abc import ABCMeta, abstractmethod

from .units import _set_SI_standard
from .units import to_si, to_user_unit
from .constants import CONSTANTS


# Helper function for checking if an altitude is within the limits of an atmospheric layer
_is_altitude = lambda altitude, limit: (
    True if altitude <= limit[1] and altitude >= limit[0] else False
)


class AtmosphericLayer(metaclass=ABCMeta):
    """
    Abstract base class for ISA atmospheric layers.

    Each atmospheric layer must implement temperature and pressure
    as functions of altitude.

    Attributes
    ----------
    lapse_rate : float
        Temperature lapse rate of the layer.

    Notes
    -----
    This class should not be instantiated directly.
    """

    lapse_rate: float = 0.0

    @property
    @abstractmethod
    def temperature(self):
        """
        Temperature at the current altitude.

        Returns
        -------
        temperature
            Temperature corresponding to the altitude within the layer.
        """
        return

    @property
    @abstractmethod
    def pressure(self):
        """
        Pressure at the current altitude.

        Returns
        -------
        pressure
            Pressure corresponding to the altitude within the layer.
        """
        return


class IsothermalLayer(AtmosphericLayer):
    """
    Base class for ISA isothermal atmospheric layers.

    In an isothermal layer, temperature does not vary with altitude.

    Parameters
    ----------
    parent : ISA
        Parent ISA instance providing altitude and unit context.

    Attributes
    ----------
    lapse_rate : float
        Temperature lapse rate (zero for isothermal layers).
    parent : ISA
        Reference to the owning ISA instance.
    """

    lapse_rate: float = 0.0

    def __init__(self, parent):
        self.parent = parent

    @property
    def temperature(self):
        """
        Temperature within the isothermal layer.

        Returns
        -------
        temperature
            Constant temperature value.
        """
        return

    @property
    def temperature_ratio(self):
        """
        Ratio of layer temperature to sea-level temperature.

        Returns
        -------
        ratio : float
            Temperature ratio.
        """
        return

    @property
    def pressure(self):
        """
        Pressure within the isothermal layer.

        Returns
        -------
        pressure
            Pressure corresponding to altitude.
        """
        return


class ISATropopause(AtmosphericLayer):
    """
    ISA tropopause atmospheric layer (11 km – 25 km).

    The tropopause is an isothermal layer where temperature
    remains constant with altitude.

    Parameters
    ----------
    parent : ISA
        Parent ISA instance.

    Attributes
    ----------
    base_temperature
        Temperature at the base of the tropopause.
    base_pressure
        Pressure at the base of the tropopause.
    base_density
        Density at the base of the tropopause.
    base_height
        Base altitude of the tropopause layer.
    """

    base_temperature = _set_SI_standard(quantity="TEMPERATURE", value=216.65)
    base_pressure = _set_SI_standard(quantity="PRESSURE", value=22632.06)
    base_density = _set_SI_standard(quantity="DENSITY", value=0.36391)
    base_height = _set_SI_standard(quantity="DISTANCE", value=11)

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        altitude = to_user_unit(self.parent.altitude.value, "DISTANCE")
        return f"ISA Tropopause({altitude})"

    @property
    def temperature(self):
        """
        Temperature within the tropopause layer.

        Returns
        -------
        temperature
            Temperature at the specified altitude.
        """
        temp = self.base_temperature + self.parent.offset
        return to_user_unit(quantity="TEMPERATURE", x=temp)

    @property
    def __exp_num(self):
        """
        Internal exponential term for pressure computation.

        Returns
        -------
        value : float
            Exponential coefficient.
        """
        height_diff = (
            self.parent.altitude - self.base_height
        ) * 1000
        num = -1 * CONSTANTS.g / (CONSTANTS.R * self.base_temperature)
        return num * height_diff

    @property
    def pressure(self):
        """
        Pressure within the tropopause layer.

        Returns
        -------
        pressure
            Pressure at the specified altitude.
        """
        log_pressure = math.log(self.base_pressure.value) + self.__exp_num
        pressure = math.exp(log_pressure)
        return to_user_unit(quantity="PRESSURE", x=pressure)


class ISATroposphere(AtmosphericLayer):
    """
    ISA troposphere atmospheric layer (0 km – 11 km).

    The troposphere exhibits a negative temperature lapse rate.

    Parameters
    ----------
    parent : ISA
        Parent ISA instance.
    """

    lapse_rate = _set_SI_standard(quantity="LAPSE_RATE", value=-0.0065)

    def __init__(self, parent):
        self.parent = parent
        self.base_temperature = CONSTANTS.MSL_TEMPERATURE

    def __repr__(self):
        altitude = to_user_unit(self.parent.altitude.value, "DISTANCE")
        return f"ISA Troposhere({altitude})"

    @property
    def temperature(self):
        """
        Temperature within the troposphere.

        Returns
        -------
        temperature
            Temperature at the specified altitude.
        """
        temp = (
            self.base_temperature.value
            + (
                ISATroposphere.lapse_rate
                * self.parent.altitude
                * 1000
            ).value
        )
        return to_user_unit(quantity="TEMPERATURE", x=temp + self.parent.offset)

    @property
    def __temperature_ratio(self):
        """
        Internal temperature ratio helper.

        Returns
        -------
        ratio : float
            Temperature ratio relative to sea level.
        """
        return (
            to_si(x=self.temperature.value, quantity="TEMPERATURE")
            / self.base_temperature.value
        )

    @property
    def pressure(self):
        """
        Pressure within the troposphere.

        Returns
        -------
        pressure
            Pressure at the specified altitude.
        """
        exp = -1 * CONSTANTS.g / (CONSTANTS.R * ISATroposphere.lapse_rate)
        res = CONSTANTS.MSL_PRESSURE * (self.__temperature_ratio ** exp.value)
        return to_user_unit(quantity="PRESSURE", x=res.value)


class ISAStratosphere(AtmosphericLayer):
    """
    ISA stratosphere atmospheric layer (20 km – 47 km).

    The stratosphere is divided into lower and upper regions,
    each with different lapse rates.

    Parameters
    ----------
    parent : ISA
        Parent ISA instance.
    """

    lapse_rate = _set_SI_standard(quantity="LAPSE_RATE", value=0.0010)
    base_temp = _set_SI_standard(quantity="TEMPERATURE", value=216.65)
    base_pressure = _set_SI_standard(quantity="PRESSURE", value=5474.89)

    def __init__(self, parent):
        self.__is_lower_strat = True
        self.parent = parent

        if _is_altitude(self.parent.altitude, (20.0, 32, 0)):
            self.__is_lower_strat = True
        else:
            self.__is_lower_strat = False
            self.lapse_rate = _set_SI_standard(quantity="LAPSE_RATE", value=0.0028)
            self.base_temp = _set_SI_standard(quantity="TEMPERATURE", value=228.65)
            self.base_pressure = _set_SI_standard(quantity="PRESSURE", value=868.02)

    def __repr__(self):
        altitude = to_user_unit(self.parent.altitude.value, "DISTANCE")
        return f"ISAStratosphere({altitude})"

    @property
    def temperature(self):
        """
        Temperature within the stratosphere.

        Returns
        -------
        temperature
            Temperature at the specified altitude.
        """
        base_height = (
            _set_SI_standard(quantity="DISTANCE", value=32.0)
            if not self.__is_lower_strat
            else _set_SI_standard(quantity="DISTANCE", value=20.0)
        )

        res = (
            self.base_temp.value
            + (
                self.lapse_rate
                * (self.parent.altitude * 1000.0 - base_height * 1000.0)
            ).value
        ) + self.parent.offset

        return to_user_unit(quantity="TEMPERATURE", x=res)

    @property
    def pressure(self):
        """
        Pressure within the stratosphere.

        Returns
        -------
        pressure
            Pressure at the specified altitude.
        """
        temp_ratio = (
            to_si(x=self.temperature.value, quantity="TEMPERATURE") / self.base_temp
        )
        exp = -1 * CONSTANTS.g / (CONSTANTS.R * self.lapse_rate)
        res = self.base_pressure * (temp_ratio ** exp.value)
        return to_user_unit(quantity="PRESSURE", x=res.value)


def _choose_atmosphere(altitude):
    """
    Select the appropriate ISA atmospheric layer.

    Parameters
    ----------
    altitude
        Geopotential altitude in kilometers (SI).

    Returns
    -------
    layer : AtmosphericLayer
        Atmospheric layer class.

    Raises
    ------
    Exception
        If altitude exceeds stratospheric limits.
    """
    if _is_altitude(altitude, (0.0, 11.0)):
        return ISATroposphere
    elif _is_altitude(altitude, (11.0, 20.0)):
        return ISATropopause
    elif _is_altitude(altitude, (20.0, 47.0)):
        return ISAStratosphere
    else:
        raise Exception(
            "This atmosphere is only valid at altitudes within or below the stratosphere"
        )


class ISA:
    """
    International Standard Atmosphere (ISA) model.

    Provides access to atmospheric properties as a function
    of altitude.

    Parameters
    ----------
    offset : float, optional
        Temperature offset applied to all layers.
    geopotential_height : float, optional
        Geopotential altitude.

    Notes
    -----
    Altitude inputs are converted internally to SI units.
    """

    atmosphere = None
    msl_density = CONSTANTS.MSL_DENSITY
    msl_pressure = CONSTANTS.MSL_PRESSURE
    msl_temperature = CONSTANTS.MSL_TEMPERATURE
    msl_gamma: float = CONSTANTS.y
    msl_dynamic_viscosity = CONSTANTS.MSL_DYNAMIC_VISCOSITY

    @classmethod
    def from_geometric_height(cls, offset: float = 0.0, geometric_height: float = 0.0):
        """
        Construct ISA model from geometric altitude.

        Parameters
        ----------
        offset : float, optional
            Temperature offset.
        geometric_height : float
            Geometric altitude.

        Returns
        -------
        ISA
            ISA instance.
        """
        Hg = cls.geopotential_height(geometric_height=geometric_height)
        return cls(offset=offset, geopotential_height=Hg.value)

    @staticmethod
    def geopotential_height(geometric_height: int | float):
        """
        Convert geometric height to geopotential height.

        Parameters
        ----------
        geometric_height : float
            Geometric altitude.

        Returns
        -------
        height
            Geopotential altitude.
        """
        h = to_si(geometric_height, "DISTANCE")
        num = CONSTANTS.r * h
        val = num / (CONSTANTS.r + h.value)
        return to_user_unit(x=val.value, quantity="DISTANCE")

    def __init__(self, *, offset: float = 0.0, geopotential_height: float = 0.0):
        """
        Initialize the ISA model.

        Parameters
        ----------
        offset : float, optional
            Temperature offset.
        geopotential_height : float, optional
            Geopotential altitude.
        """
        self.offset = offset
        self.altitude = to_si(geopotential_height, "DISTANCE")
        self.__atmosphere_layer(altitude=self.altitude)

    def __getattr__(self, name):
        """
        Delegate attribute access to the active atmospheric layer.
        """
        if hasattr(self.__class__, name):
            return getattr(self, name)
        return getattr(self.atmosphere, name)

    def __add__(self, offset: int):
        """Increase temperature offset."""
        self.offset += offset

    def __sub__(self, offset: int):
        """Decrease temperature offset."""
        self.offset -= offset

    def __repr__(self):
        altitude = to_user_unit(self.altitude.value, "DISTANCE")
        return f"ISA({self.offset, altitude})"

    @property
    def density(self):
        """
        Air density at the current altitude.

        Returns
        -------
        density
            Air density.
        """
        denum = CONSTANTS.R * to_si(
            x=self.atmosphere.temperature.value, quantity="TEMPERATURE"
        )
        res = to_si(x=self.atmosphere.pressure.value, quantity="PRESSURE") / denum
        return to_user_unit(res.value, "DENSITY")

    @property
    def temperature_ratio(self):
        """
        Ratio of local temperature to sea-level temperature.

        Returns
        -------
        ratio : float
            Temperature ratio.
        """
        val = self.atmosphere.temperature
        return to_si(x=val.value, quantity="TEMPERATURE") / _set_SI_standard(
            value=self.msl_temperature.value, quantity="TEMPERATURE"
        )

    @property
    def density_ratio(self):
        """
        Ratio of local density to sea-level density.

        Returns
        -------
        ratio : float
            Density ratio.
        """
        return self.density / to_user_unit(self.msl_density.value, "DENSITY")

    @property
    def pressure_ratio(self):
        """
        Ratio of local pressure to sea-level pressure.

        Returns
        -------
        ratio : float
            Pressure ratio.
        """
        return self.atmosphere.pressure / to_user_unit(
            self.msl_pressure.value, "PRESSURE"
        )

    @property
    def geometric_height(self):
        """
        Convert geopotential altitude to geometric altitude.

        Returns
        -------
        height
            Geometric altitude.
        """
        denum = CONSTANTS.r - self.altitude
        res = (CONSTANTS.r * self.altitude).value / denum
        return to_user_unit(res, "DISTANCE")

    @property
    def dynamic_viscosity(self):
        """
        Dynamic viscosity of air.

        Returns
        -------
        viscosity
            Dynamic viscosity.
        """
        expr_3_1 = self.msl_temperature + CONSTANTS.S
        expr_3_2 = self.atmosphere.temperature + CONSTANTS.S
        res = (
            CONSTANTS.MSL_DYNAMIC_VISCOSITY
            * (self.temperature_ratio ** (3 / 2))
            * (expr_3_1 / expr_3_2)
        ).value
        return _set_SI_standard(quantity="DYNAMIC_VISCOSITY", value=res)

    @property
    def kinematic_viscosity(self):
        """
        Kinematic viscosity of air.

        Returns
        -------
        viscosity
            Kinematic viscosity.
        """
        res = self.dynamic_viscosity / self.density
        return _set_SI_standard(quantity="KINEMATIC_VISCOSITY", value=res.value)

    @property
    def speed_of_sound(self):
        """
        Speed of sound at the current altitude.

        Returns
        -------
        speed
            Speed of sound.
        """
        temperature = to_si(
            x=self.atmosphere.temperature.value, quantity="TEMPERATURE"
        )
        res = (temperature.value * CONSTANTS.R.value * self.msl_gamma) ** 0.5
        return to_user_unit(res, "SPEED")

    def mach_number(self, velocity):
        """
        Compute Mach number for a given velocity.

        Parameters
        ----------
        velocity : float
            Velocity in user-defined units.

        Returns
        -------
        mach : float
            Mach number.
        """
        velocity = to_si(velocity, "SPEED")
        return velocity / to_si(x=self.speed_of_sound.value, quantity="SPEED")

    def dynamic_pressure(self, velocity):
        """
        Compute dynamic pressure.

        Parameters
        ----------
        velocity : float
            Velocity in user-defined units.

        Returns
        -------
        pressure
            Dynamic pressure.
        """
        velocity = to_si(velocity, "SPEED")
        res = (
            0.5 * to_si(x=self.density.value, quantity="DENSITY") * (velocity ** 2)
        ).value
        return to_user_unit(res, "PRESSURE")

    def __atmosphere_layer(self, altitude):
        """
        Configure the appropriate atmospheric layer.
        """
        self.atmosphere = _choose_atmosphere(altitude)(self)
