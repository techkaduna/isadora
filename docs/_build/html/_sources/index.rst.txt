===========================================================
Isadora ISA Documentation
===========================================================

Welcome to the **Isadora ISA** documentation!
==============================================

.. raw:: html
   <hr style='border-top: 3px dashed #43a047; margin: 30px 0'>

Isadora is a lightweight, precise, and Pythonic implementation of the
International Standard Atmosphere (ISA) model. It allows users to compute
atmospheric properties including temperature, pressure, density, dynamic
and kinematic viscosity, and speed of sound for any geopotential altitude.
The package is ICAO 1983 compliant.

It is designed for aerospace engineers, researchers, and students needing
reliable, unit-aware atmospheric computations in Python.

Features
--------

- Unit-aware computations for atmospheric properties.
- Derived quantities: Mach number, dynamic pressure, geometric height.
- Multiple unit systems: SI (default), USCS, Imperial.
- Physical constants and properties implemented as type-safe objects.
- Validation against ICAO 1983 reference tables.
- Easily extensible for advanced flight performance computations.

.. contents::
   :local:
   :depth: 2
   :backlinks: top

Installation
------------

Install directly from PyPI:

.. code-block:: bash

    pip install isadora

Or clone the repository and install locally:

.. code-block:: bash

    git clone https://github.com/techkaduna/isadora.git
    cd isadora
    pip install .

Quick Start
-----------

Creating an ISA atmosphere at a specific altitude:

.. code-block:: python

    from isadora import ISA

    # Create an atmosphere at 5 km geopotential height
    atm = ISA(geopotential_height=5)

    # Access standard atmospheric properties
    print("Temperature:", atm.temperature)
    print("Pressure:", atm.pressure)
    print("Density:", atm.density)
    print("Dynamic viscosity:", atm.dynamic_viscosity)
    print("Kinematic viscosity:", atm.kinematic_viscosity)
    print("Speed of sound:", atm.speed_of_sound)
    print("Atmospheric layer:", atm.atmosphere)

Unit Systems
------------

ISADORA supports SI, USCS, and Imperial units. You can set the global
unit standard:

.. code-block:: python

    from isadora.units import UnitRegistry

    # Set unit system globally
    UnitRegistry.set_unit_standard("USCS")
    
    # now import the needed class
    from isadora import ISA

    atm = ISA(geopotential_height=5)
    print("Temperature in Fahrenheit:", atm.temperature)

Physical Constants
------------------

All physical constants are centralized in the `CONSTANTS` object:

- `MSL_TEMPERATURE` — Standard sea-level temperature
- `MSL_PRESSURE` — Standard sea-level pressure
- `MSL_DENSITY` — Sea-level air density
- `MSL_DYNAMIC_VISCOSITY` — Sea-level dynamic viscosity
- `MSL_KINEMATIC_VISCOSITY` — Sea-level kinematic viscosity
- `g` — Acceleration due to gravity
- `R` — Specific gas constant for dry air
- `R_` — Universal gas constant
- `M` — Molar mass of dry air
- `a_o` — Speed of sound at sea level
- `y` — Ratio of specific heats (gamma)
- `c_p` — Specific heat at constant pressure
- `c_v` — Specific heat at constant volume
- `S` — Sutherland’s constant for air viscosity

Any of these constants can be accessed as follows:

.. code-block:: python

    from isadora import CONSTANTS

    a_o = CONSTANTS.a_o

Usage Guide
-----------

Creating an ISA Atmosphere Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`ISA` objects are initialized with the following parameters:

- `geopotential_height` (float): Altitude in km.
- `offset` (float, optional): Temperature deviation from standard ISA (K).

.. code-block:: python

    atm = ISA(geopotential_height=10, offset=5)

Accessing Atmospheric Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`ISA` exposes several properties:

- `temperature` — Air temperature (unit-aware)
- `pressure` — Air pressure (unit-aware)
- `density` — Air density (unit-aware)
- `dynamic_viscosity` — Dynamic viscosity
- `kinematic_viscosity` — Kinematic viscosity
- `speed_of_sound` — Local speed of sound
- `layer` — Atmospheric layer (Troposphere, Tropopause, Stratosphere)

Derived Flight Quantities
~~~~~~~~~~~~~~~~~~~~~~~~

- `dynamic_pressure(velocity)` — Computes `q = 0.5 * rho * V^2`.
- `mach_number(velocity)` — Computes Mach number at given velocity.
- `geometric_height` — Converts geopotential height to geometric height.

.. code-block:: python

    V = 250  # m/s
    q = atm.dynamic_pressure(V)
    M = atm.mach_number(V)
    print("Dynamic pressure:", q)
    print("Mach number:", M)

Temperature Offsets
~~~~~~~~~~~~~~~~~~~

Apply non-standard conditions by specifying `offset` in the constructor:

.. code-block:: python

    atm_offset = ISA(geopotential_height=10, offset=10)
    print(atm_offset.temperature)  # ISA + 10 K

Plotting Atmospheric Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can generate profiles of temperature, pressure, density:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from isadora import ISA

    h = np.linspace(0, 20, 201)
    T, P, rho = [], [], []

    for hi in h:
        isa = ISA(geopotential_height=hi)
        T.append(isa.temperature)
        P.append(isa.pressure)
        rho.append(isa.density)

    plt.plot(T, h, label="Temperature (K)")
    plt.plot(P, h, label="Pressure (Pa)")
    plt.plot(rho, h, label="Density (kg/m³)")
    plt.xlabel("Value")
    plt.ylabel("Geopotential Height (km)")
    plt.title("ISA 1983 Atmospheric Profiles")
    plt.grid(True)
    plt.legend()
    plt.show()

Unit Conversion Utilities
~~~~~~~~~~~~~~~~~~~~~~~~

- `UnitRegistry.set_unit_standard()` — Set SI, USCS, Imperial.
- `to_si(value, quantity)` — Convert from active unit to SI.
- `to_user_unit(value, quantity)` — Convert from SI to active unit.

Testing
-------

Unit tests validate:

- ICAO 1983 compliance
- Edge cases
- Type safety and unit conversions

Run tests:

.. code-block:: bash

    pytest tests/

Credits
-------

- The ISADORA logo was generated by ChatGPT.
- The Documentation was authored with ChatGPT assistance.

.. note::

    All calculations assume **geopotential altitude** unless otherwise stated.
    SI units are default; conversions to USCS or Imperial are supported.

.. raw:: html
   <hr style='border-top: 3px dashed #43a047; margin: 30px 0'>

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   examples
   changelog
   contributing

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. raw:: html
   <hr style='border-top: 3px dashed #43a047; margin: 30px 0'>
