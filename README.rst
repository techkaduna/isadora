.. figure:: https://raw.githubusercontent.com/techkaduna/isadora/main/isadora.svg
   :alt: isadora logo

   isadora logo

ISADORA - ICAO 1983 Compliant International Standard Atmosphere (ISA)
====================================================================

**Isadora** is a lightweight, precise, and Pythonic implementation of the
International Standard Atmosphere (ISA) model. It provides **atmospheric properties**
(temperature, pressure, density, dynamic and kinematic viscosity, speed of sound)
at any geopotential altitude.  

The package is fully **unit-aware**, supporting **SI**, **USCS**, and **Imperial** units, 
and validated against ICAO 1983 reference tables.

Ideal for aerospace engineers, researchers, and students, Isadora simplifies
atmospheric computations while ensuring accuracy and unit safety.

Features
--------

- Compute **unit-aware atmospheric properties** at any geopotential height.
- Compute **derived quantities**: Mach number, dynamic pressure, geometric height.
- Support for multiple unit systems: SI (default), USCS, Imperial.
- **Physical constants** implemented using type-safe, immutable units.
- Fully **ICAO 1983 compliant** calculations.
- **Pytest-tested** for physical consistency, numerical correctness, and unit integrity.

Installation
------------

Install via `pip`:

.. code-block:: bash

    pip install isadora

Or clone the repository and install locally:

.. code-block:: bash

    git clone https://github.com/techkaduna/isadora.git
    cd isadora
    pip install .

Dependencies
------------

- Python >= 3.10
- `mudu` – unit and measurement library
- `dataclasses` (Python 3.10+ has it built-in)
- `pytest` – for running the test suite

Quick Start
-----------

Import the package and create an ISA atmosphere:

.. code-block:: python

    from isadora import ISA

    # Create an ISA atmosphere at 5 km geopotential height
    atm = ISA(geopotential_height=5)

    print("Temperature:", atm.temperature)
    print("Pressure:", atm.pressure)
    print("Density:", atm.density)
    print("Dynamic Viscosity:", atm.dynamic_viscosity)
    print("Kinematic Viscosity:", atm.kinematic_viscosity)
    print("Speed of Sound:", atm.speed_of_sound)
    print("Mach Number at 20 m/s:", atm.mach_number(20))
    print("Geometric Height:", atm.geometric_height)

Switching Units
---------------

Change the global unit system using `UnitRegistry`:

.. code-block:: python

    from isadora.units import UnitRegistry

    # Set to USCS units
    UnitRegistry.set_unit_standard("USCS")

    atm_uscs = ISA(geopotential_height=10)
    print("Temperature (USCS):", atm_uscs.temperature)
    print("Pressure (USCS):", atm_uscs.pressure)

Derived Quantities
------------------

The `ISA` object provides convenient methods:

- `atm.mach_number(velocity)` – computes Mach number for a given velocity.
- `atm.dynamic_pressure(velocity)` – computes dynamic pressure at altitude.
- `atm.geometric_height` – converts geopotential height to geometric height.
- `atm.speed_of_sound` – sound speed at the specified altitude.

Testing
-------

Run the full **Pytest** test suite:

.. code-block:: bash

    pytest -v tests/

Tests cover:

- ICAO 1983 reference validation
- Physical consistency (hydrostatic equilibrium, monotonicity)
- Derived quantities (Mach, dynamic pressure, geometric height)
- Unit system correctness and conversion


References
----------

- International Civil Aviation Organization (ICAO), 1983, *Standard Atmosphere Tables*
- U.S. Standard Atmosphere, 1976, NASA

License
-------

MIT License. See LICENSE file for details.

Contributing
------------

Contributions are welcome! Follow **PEP 8** style, include tests for new features,
and submit via GitHub Pull Requests.

Contact
-------

Author: Kolawole Andrew  
GitHub: `https://github.com/techkaduna/isadora`  
Email: `andrewolakola@gmail.com`
