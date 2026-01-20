"""
isadora.units
=============

Unit system and unit-conversion utilities for the ISADORA package.

This module defines:
- Physical unit definitions
- Unit standards (SI, USCS, Imperial)
- A global unit registry
- Conversion helpers between SI and user-defined units
- Internal descriptors for unit-aware constants

All numerical calculations within ISADORA are performed in SI units.
This module provides transparent conversion to and from user-selected
unit systems.

Notes
-----
- Unit handling is based on the ``mudu`` package.
- The unit standard can be set only once per runtime.
- This module is foundational and imported by most other submodules.

Classes
-------
QuantityTable
UnitRegistry
_UnitParam

Functions
---------
to_si
to_user_unit

Attributes
----------
si_units
uscs_units
imperial_units
si
uscs
imperial
"""

import functools
from typing import Callable, Dict
from dataclasses import dataclass, field

from mudu import Length, FEET, METER
from mudu import SECOND
from mudu import POUND, SLUG
from mudu import Temperature, FARENHEIT, CELSIUS, KELVIN
from mudu import KILOGRAM, KILOMETER, GenericUnit2
from mudu import (
    Density,
    KILOGRAM_PER_CUBIC_METER,
    SLUG_PER_CUBIC_FOOT,
    POUND_PER_CUBIC_FOOT,
)
from mudu import Pressure, PASCAL, inHg, POUND_PER_SQUARE_FOOT
from mudu import JOULE, MOLE, _UnitType


@dataclass
class QuantityTable:
    """
    Container mapping physical quantities to unit constructors.

    This dataclass groups callable constructors for each physical
    quantity under a given unit standard (SI, USCS, Imperial).

    Attributes
    ----------
    UNIT_NAME : str
        Name of the unit system.
    TEMPERATURE : Callable
        Temperature unit constructor.
    DENSITY : Callable
        Density unit constructor.
    PRESSURE : Callable
        Pressure unit constructor.
    DISTANCE : Callable
        Length / distance unit constructor.
    DYNAMIC_VISCOSITY : Callable
        Dynamic viscosity unit constructor.
    KINEMATIC_VISCOSITY : Callable
        Kinematic viscosity unit constructor.
    SPEED : Callable
        Speed unit constructor.
    LAPSE_RATE : Callable
        Temperature lapse-rate unit constructor.
    UNIV_GAS_CONSTANT : Callable
        Universal gas constant unit constructor.
    EARTH_MOLAR_MASS : Callable
        Earth molar mass unit constructor.
    SPEC_HEAT_CONSTANT : Callable
        Specific heat constant unit constructor.
    """

    UNIT_NAME: str
    TEMPERATURE: Callable
    DENSITY: Callable
    PRESSURE: Callable
    DISTANCE: Callable
    DYNAMIC_VISCOSITY: Callable
    KINEMATIC_VISCOSITY: Callable
    SPEED: Callable
    LAPSE_RATE: Callable
    UNIV_GAS_CONSTANT: Callable
    EARTH_MOLAR_MASS: Callable
    SPEC_HEAT_CONSTANT: Callable


# ============================================================================
# SPEED UNITS
# ============================================================================
METER_PER_SECOND = METER / SECOND
FEET_PER_SECOND = FEET / SECOND
KNOT = _UnitType(
    _dimension="speed",
    _unit_name="knot",
    _unit_symbol="kn",
    _order=None,
)

# ============================================================================
# LAPSE RATE UNITS
# ============================================================================
KELVIN_PER_METER = KELVIN / METER
FARENHEIT_PER_FEET = FARENHEIT / FEET
CELSIUS_PER_FEET = CELSIUS / FEET

# ============================================================================
# DYNAMIC VISCOSITY UNITS
# ============================================================================
KILOGRAM_PER_METER_SECOND = KILOGRAM / (METER * SECOND)
SLUG_PER_FEET_SECOND = SLUG / (FEET * SECOND)
POUND_PER_FEET_SECOND = POUND / (FEET * SECOND)

# ============================================================================
# KINEMATIC VISCOSITY UNITS
# ============================================================================
METER_SQR_PER_SECOND = (METER**2) / SECOND
FEET_PER_SQR_SECOND = (FEET**2) / SECOND

# ============================================================================
# SPECIFIC HEAT CONSTANT
# ============================================================================
JOULE_PER_KILOGRAM_KELVIN = JOULE / (KILOGRAM * KELVIN)

# ============================================================================
# UNIVERSAL GAS CONSTANT
# ============================================================================
JOULE_PER_MOL_KELVIN = JOULE / (MOLE * KELVIN)

# ============================================================================
# EARTH MOLAR MASS
# ============================================================================
KILOGRAM_PER_MOL = KILOGRAM / MOLE


_make_unit = lambda unit: functools.partial(GenericUnit2, unit_definition=unit)
"""
Internal helper to construct GenericUnit2 callables.
"""


# ============================================================================
# UNIT STANDARD DEFINITIONS
# ============================================================================
si_units = {
    "UNIT_NAME": "SI",
    "TEMPERATURE": KELVIN,
    "DENSITY": KILOGRAM_PER_CUBIC_METER,
    "PRESSURE": PASCAL,
    "DISTANCE": KILOMETER,
    "DYNAMIC_VISCOSITY": KILOGRAM_PER_METER_SECOND,
    "KINEMATIC_VISCOSITY": METER_SQR_PER_SECOND,
    "SPEED": METER_PER_SECOND,
    "LAPSE_RATE": KELVIN_PER_METER,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}

uscs_units = {
    "UNIT_NAME": "USCS",
    "TEMPERATURE": FARENHEIT,
    "DENSITY": SLUG_PER_CUBIC_FOOT,
    "PRESSURE": inHg,
    "DISTANCE": FEET,
    "DYNAMIC_VISCOSITY": SLUG_PER_FEET_SECOND,
    "KINEMATIC_VISCOSITY": FEET_PER_SQR_SECOND,
    "SPEED": FEET_PER_SECOND,
    "LAPSE_RATE": FARENHEIT_PER_FEET,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}

imperial_units = {
    "UNIT_NAME": "IMPERIAL",
    "TEMPERATURE": CELSIUS,
    "DENSITY": POUND_PER_CUBIC_FOOT,
    "PRESSURE": POUND_PER_SQUARE_FOOT,
    "DISTANCE": FEET,
    "DYNAMIC_VISCOSITY": POUND_PER_FEET_SECOND,
    "KINEMATIC_VISCOSITY": FEET_PER_SQR_SECOND,
    "SPEED": KNOT,
    "LAPSE_RATE": CELSIUS_PER_FEET,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}


# ============================================================================
# UNIT CALLABLE TABLES
# ============================================================================
si = {
    "UNIT_NAME": "SI",
    "TEMPERATURE": functools.partial(Temperature, unit=si_units["TEMPERATURE"]),
    "DENSITY": functools.partial(Density, unit_definition=si_units["DENSITY"]),
    "PRESSURE": functools.partial(Pressure, unit_definition=si_units["PRESSURE"]),
    "DISTANCE": functools.partial(Length, unit=si_units["DISTANCE"]),
    "DYNAMIC_VISCOSITY": _make_unit(si_units["DYNAMIC_VISCOSITY"]),
    "KINEMATIC_VISCOSITY": _make_unit(si_units["KINEMATIC_VISCOSITY"]),
    "SPEED": _make_unit(si_units["SPEED"]),
    "LAPSE_RATE": _make_unit(si_units["LAPSE_RATE"]),
    "UNIV_GAS_CONSTANT": _make_unit(si_units["UNIV_GAS_CONSTANT"]),
    "EARTH_MOLAR_MASS": _make_unit(si_units["EARTH_MOLAR_MASS"]),
    "SPEC_HEAT_CONSTANT": _make_unit(si_units["SPEC_HEAT_CONSTANT"]),
}

uscs = {
    "UNIT_NAME": "USCS",
    "TEMPERATURE": functools.partial(Temperature, unit=uscs_units["TEMPERATURE"]),
    "DENSITY": functools.partial(Density, unit_definition=uscs_units["DENSITY"]),
    "PRESSURE": functools.partial(Pressure, unit_definition=uscs_units["PRESSURE"]),
    "DISTANCE": functools.partial(Length, unit=uscs_units["DISTANCE"]),
    "DYNAMIC_VISCOSITY": _make_unit(uscs_units["DYNAMIC_VISCOSITY"]),
    "KINEMATIC_VISCOSITY": _make_unit(uscs_units["KINEMATIC_VISCOSITY"]),
    "SPEED": _make_unit(uscs_units["SPEED"]),
    "LAPSE_RATE": _make_unit(uscs_units["LAPSE_RATE"]),
    "UNIV_GAS_CONSTANT": _make_unit(uscs_units["UNIV_GAS_CONSTANT"]),
    "EARTH_MOLAR_MASS": _make_unit(uscs_units["EARTH_MOLAR_MASS"]),
    "SPEC_HEAT_CONSTANT": _make_unit(uscs_units["SPEC_HEAT_CONSTANT"]),
}

imperial = {
    "UNIT_NAME": "IMPERIAL",
    "TEMPERATURE": functools.partial(Temperature, unit=imperial_units["TEMPERATURE"]),
    "DENSITY": functools.partial(Density, unit_definition=imperial_units["DENSITY"]),
    "PRESSURE": functools.partial(Pressure, unit_definition=imperial_units["PRESSURE"]),
    "DISTANCE": functools.partial(Length, unit=imperial_units["DISTANCE"]),
    "DYNAMIC_VISCOSITY": _make_unit(imperial_units["DYNAMIC_VISCOSITY"]),
    "KINEMATIC_VISCOSITY": _make_unit(imperial_units["KINEMATIC_VISCOSITY"]),
    "SPEED": _make_unit(imperial_units["SPEED"]),
    "LAPSE_RATE": _make_unit(imperial_units["LAPSE_RATE"]),
    "UNIV_GAS_CONSTANT": _make_unit(imperial_units["UNIV_GAS_CONSTANT"]),
    "EARTH_MOLAR_MASS": _make_unit(imperial_units["EARTH_MOLAR_MASS"]),
    "SPEC_HEAT_CONSTANT": _make_unit(imperial_units["SPEC_HEAT_CONSTANT"]),
}


@dataclass
class UnitRegistry:
    """
    Global unit registry and standard selector.

    This class manages the active unit standard for the entire package.
    The unit standard can be set exactly once per runtime.

    Attributes
    ----------
    STANDARDS : tuple of str
        Supported unit standards.
    """

    STANDARDS = ("SI", "USCS", "IMPERIAL")
    _unit_standard: str = field(default="SI", init=False, repr=False)
    _locked: bool = field(default=False, init=False, repr=False)

    SI = QuantityTable(**si)
    USCS = QuantityTable(**uscs)
    IMPERIAL = QuantityTable(**imperial)

    SI_UNITS = si_units
    USCS_UNITS = uscs_units
    IMPERIAL_UNITS = imperial_units

    _unit_mapping = dict(zip(STANDARDS, [SI, USCS, IMPERIAL]))
    _unit_std_mapping = dict(zip(STANDARDS, [SI_UNITS, USCS_UNITS, IMPERIAL_UNITS]))

    @classmethod
    def set_unit_standard(cls, standard: str):
        """
        Set the global unit standard.

        Parameters
        ----------
        standard : str
            One of ``"SI"``, ``"USCS"``, or ``"IMPERIAL"``.

        Raises
        ------
        RuntimeError
            If the unit standard has already been set.
        ValueError
            If the provided standard is invalid.
        """
        standard = standard.upper()

        if cls._locked:
            raise RuntimeError(
                f"Unit standard has already been set to {cls._unit_standard}"
            )

        if standard not in cls.STANDARDS:
            raise ValueError(f"{standard} is not an available unit standard")

        cls._unit_standard = standard
        cls._locked = True

    @classmethod
    def get_units(cls) -> QuantityTable:
        """
        Get the active unit constructors.

        Returns
        -------
        QuantityTable
            Unit constructor table for the active standard.
        """
        return cls._unit_mapping[cls._unit_standard]

    @classmethod
    def get_unit_standard(cls) -> Dict:
        """
        Get the active unit definition mapping.

        Returns
        -------
        dict
            Mapping of quantity names to unit definitions.
        """
        return cls._unit_std_mapping[cls._unit_standard]


_set_SI_standard = lambda quantity, value: si.get(quantity)(value)
"""
Internal helper to construct SI-unit quantities.
"""


class _UnitParam:
    """
    Descriptor for immutable, unit-aware parameters.

    This descriptor allows attributes to be assigned once and
    automatically converted to SI units.

    Parameters
    ----------
    name : str
        Attribute name.
    quantity : str
        Physical quantity type.
    """

    def __init__(self, name: str, quantity: str) -> None:
        self.name = name
        self.quantity = quantity

    def __get__(self, instance, cls):
        if instance is None:
            return self

        if self.name not in instance.__dict__:
            raise AttributeError(f"{self.name} has not been set.")

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise RuntimeError(f"{self.name} is a constant and cannot be changed.")

        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be of type int or float")

        instance.__dict__[self.name] = si[self.quantity](value)


def to_si(x: float, quantity: str):
    """
    Convert a value from the active unit system to SI.

    Parameters
    ----------
    x : float
        Value in user-defined units.
    quantity : str
        Physical quantity name.

    Returns
    -------
    value
        Value converted to SI units.
    """
    unit_standard = UnitRegistry.get_unit_standard()
    val = getattr(UnitRegistry.get_units(), quantity.upper())(x)

    if unit_standard["UNIT_NAME"] != "SI":
        return val.convert_to(si_units[quantity.upper()])
    return val


def to_user_unit(x, quantity: str):
    """
    Convert a value from SI units to the active user unit system.

    Parameters
    ----------
    x : float
        Value assumed to be in SI units.
    quantity : str
        Physical quantity name.

    Returns
    -------
    value
        Value converted to the active user unit system.
    """
    value = _set_SI_standard(quantity.upper(), x)
    user_std = UnitRegistry.get_unit_standard()["UNIT_NAME"]

    if user_std == "SI":
        return value

    std = uscs_units if user_std == "USCS" else imperial_units
    return value.convert_to(std[quantity.upper()])
