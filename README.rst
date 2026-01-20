An ICAO 1983 compliant implementation of the the International Standard Atmosphere.
===============================================================

Isadora is a lightweight, precise, and Pythonic implementation of the
International Standard Atmosphere (ISA) model. It provides atmospheric
properties (temperature, pressure, density, viscosity, speed of sound)
at various altitudes, and allows conversion between multiple unit systems:
SI, USCS, and Imperial. Historical reference data (ARDC 1959) is also
available for comparison.

This package is ideal for aerospace engineers, researchers, and students
who need a simple, reliable ISA implementation in Python.

Features
--------

- Compute unit-aware standard atmosphere properties at any geopotential height.
- Derived quantities: Mach number, dynamic pressure, geometric height.
- Supports multiple unit systems:
  - SI (default)
  - USCS
  - Imperial
- Internal constants and physical properties implemented using type-safe units.
- Validated against ICAO 1983 reference tables.
- Optional comparison against ARDC 1959 historical data.
- Fully tested with Pytest for physical consistency and numerical correctness.

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
- `mudu` – Unit and measurement library
- `dataclasses` (Python 3.10+ has it built-in)
- `pytest` (for running tests)

Quick Start
-----------

Import the package and instantiate an ISA atmosphere:

.. code-block:: python

    from isadora import ISA

    # Create an ISA atmosphere at 5 km geopotential height
    atm = ISA(geopotential_height=5)

    print("Temperature:", atm.temperature)
    print("Pressure:", atm.pressure)
    print("Density:", atm.density)
    print("Dynamic Viscosity:", atm.dynamic_viscosity)
    print("Speed of Sound:", atm.speed_of_sound)
    print("Mach Number for 20 m/s:", atm.mach_number(20))
    print("Geometric Height:", atm.geometric_height)

Changing Unit Systems
--------------------

You can change the unit system globally using `UnitRegistry`:

.. code-block:: python

    from isadora.units import UnitRegistry

    # Set to USCS units (imperial feet, psi, slug/ft³, etc.)
    UnitRegistry.set_unit_standard("USCS")

    atm = ISA(geopotential_height=10)
    print("Temperature (USCS):", atm.temperature)
    print("Pressure (USCS):", atm.pressure)

Unit conversion is also allowed as defined in the `mudu` package documentation.

Using Historical ARDC 1959 Data
-------------------------------

You can optionally compare computed values against the ARDC 1959 reference
atmosphere:

.. code-block:: python

    from isadora.tests.test_ardc_reference import ARDC_TABLE
    from isadora import ISA

    for h, ref in ARDC_TABLE.items():
        atm = ISA(geopotential_height=h)
        print(f"Altitude: {h} km, ΔT = {atm.temperature.value - ref['T']} K")

Testing
-------

The package is fully tested using Pytest. To run the tests:

.. code-block:: bash

    pytest -v tests/

Test coverage includes:

- ICAO 1983 reference atmosphere validation
- Historical ARDC 1959 comparison
- Physical consistency (hydrostatic equilibrium, monotonicity)
- Derived quantities (speed of sound, Mach number)
- Unit system invariance and conversions

Package Structure
-----------------
isadora/
├── init.py # Package initialization
├── constants.py # Physical constants and MSL properties
├── units.py # Unit definitions, registries, and conversion functions
├── base.py # Main ISA class implementation
tests/
└── ... # Pytest tests
examples/
└── ... # usage example script


Cheat Sheet
-------------------------

This cheat sheet highlights the most common operations with the Isadora ISA
package. Copy-paste the snippets into a Python console or script to try them out.

Importing the Package
--------------------

.. code-block:: python

    from isadora import ISA
    from isadora.units import UnitRegistry

Creating an ISA Atmosphere
--------------------------

.. code-block:: python

    # Default geopotential height: 5 km
    atm = ISA(geopotential_height=5)

    # Access basic atmospheric properties
    print("Temperature:", atm.temperature)
    print("Pressure:", atm.pressure)
    print("Density:", atm.density)

Derived Quantities
------------------

.. code-block:: python

    print("Dynamic Viscosity:", atm.dynamic_viscosity)
    print("Kinematic Viscosity:", atm.kinematic_viscosity)
    print("Speed of Sound:", atm.speed_of_sound)
    print("Mach Number for 20 m/s:", atm.mach_number(20))
    print("Geometric Height:", atm.geometric_height)

Switching Unit Systems
---------------------

.. code-block:: python

    # Change global unit system
    UnitRegistry.set_unit_standard("USCS")  # Options: SI, USCS, IMPERIAL

    atm_uscs = ISA(geopotential_height=10)
    print("Temperature (USCS):", atm_uscs.temperature)
    print("Pressure (USCS):", atm_uscs.pressure)


Comparing with Historical ARDC Data
-----------------------------------

.. code-block:: python

    from isadora.tests.test_ardc_reference import ARDC_TABLE

    for h, ref in ARDC_TABLE.items():
        atm = ISA(geopotential_height=h)
        print(f"Altitude: {h} km, ΔT = {atm.temperature.value - ref['T']} K")

Running Tests
-------------

.. code-block:: bash

    # Run all tests
    pytest -v tests/

References
----------

- International Civil Aviation Organization (ICAO), 1983, *Standard Atmosphere Tables*
- ARDC 1959, *Atmospheric Reference Data* (historical dataset)
- U.S. Standard Atmosphere, 1976, NASA

License
-------

MIT License. See LICENSE file for details.

Contributing
------------

Contributions are welcome! Please submit issues or pull requests via GitHub.
Follow the PEP8 style guide and include new tests for added functionality.

Contact
-------

Author: Kolawole Andrew  
GitHub: `https://github.com/techkaduna/isadora`  
Email: `your.andrewolakola@gmail.com`
