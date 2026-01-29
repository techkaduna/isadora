isadora
=======

.. py:module:: isadora

.. autoapi-nested-parse::

   =======================
   isadora - ISA the gift.
   =======================

   An ICAO 1983 compliant implementation of the the International Standard Atmosphere.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/isadora/base/index
   /autoapi/isadora/constants/index
   /autoapi/isadora/units/index


Attributes
----------

.. autoapisummary::

   isadora.CONSTANTS


Classes
-------

.. autoapisummary::

   isadora.UnitRegistry
   isadora.ISA


Package Contents
----------------

.. py:class:: UnitRegistry

   Global unit registry and standard selector.

   This class manages the active unit standard for the entire package.
   The unit standard can be set exactly once per runtime.

   .. attribute:: STANDARDS

      Supported unit standards.

      :type: tuple of str


   .. py:attribute:: STANDARDS
      :value: ('SI', 'USCS', 'IMPERIAL')



   .. py:attribute:: _unit_standard
      :type:  str
      :value: 'SI'



   .. py:attribute:: _locked
      :type:  bool
      :value: False



   .. py:attribute:: SI


   .. py:attribute:: USCS


   .. py:attribute:: IMPERIAL


   .. py:attribute:: SI_UNITS


   .. py:attribute:: USCS_UNITS


   .. py:attribute:: IMPERIAL_UNITS


   .. py:attribute:: _unit_mapping


   .. py:attribute:: _unit_std_mapping


   .. py:method:: set_unit_standard(standard: str)
      :classmethod:


      Set the global unit standard.

      :param standard: One of ``"SI"``, ``"USCS"``, or ``"IMPERIAL"``.
      :type standard: str

      :raises RuntimeError: If the unit standard has already been set.
      :raises ValueError: If the provided standard is invalid.



   .. py:method:: get_units() -> QuantityTable
      :classmethod:


      Get the active unit constructors.

      :returns: Unit constructor table for the active standard.
      :rtype: QuantityTable



   .. py:method:: get_unit_standard() -> Dict
      :classmethod:


      Get the active unit definition mapping.

      :returns: Mapping of quantity names to unit definitions.
      :rtype: dict



.. py:data:: CONSTANTS

   Singleton instance containing all physical and atmospheric constants.

   This object should be imported and used wherever constants are
   required within the ISADORA package.

.. py:class:: ISA(*, offset: float = 0.0, geopotential_height: float = 0.0)

   International Standard Atmosphere (ISA) model.

   Provides access to atmospheric properties as a function
   of altitude.

   :param offset: Temperature offset applied to all layers.
   :type offset: float, optional
   :param geopotential_height: Geopotential altitude.
   :type geopotential_height: float, optional

   .. rubric:: Notes

   Altitude inputs are converted internally to SI units.


   .. py:attribute:: atmosphere
      :value: None



   .. py:attribute:: msl_density
      :value: 1.2250122659907



   .. py:attribute:: msl_pressure
      :value: 101325.0



   .. py:attribute:: msl_temperature
      :value: 288.15



   .. py:attribute:: msl_gamma
      :type:  float
      :value: 1.4



   .. py:attribute:: msl_dynamic_viscosity
      :value: 1.7894e-05



   .. py:method:: from_geometric_height(offset: float = 0.0, geometric_height: float = 0.0)
      :classmethod:


      Construct ISA model from geometric altitude.

      :param offset: Temperature offset.
      :type offset: float, optional
      :param geometric_height: Geometric altitude.
      :type geometric_height: float

      :returns: ISA instance.
      :rtype: ISA



   .. py:method:: geopotential_height(geometric_height: int | float)
      :staticmethod:


      Convert geometric height to geopotential height.

      :param geometric_height: Geometric altitude.
      :type geometric_height: float

      :returns: Geopotential altitude.
      :rtype: height



   .. py:attribute:: offset
      :value: 0.0



   .. py:attribute:: altitude


   .. py:method:: __getattr__(name)

      Delegate attribute access to the active atmospheric layer.



   .. py:method:: __add__(offset: int)

      Increase temperature offset.



   .. py:method:: __sub__(offset: int)

      Decrease temperature offset.



   .. py:method:: __repr__()


   .. py:property:: density

      Air density at the current altitude.

      :returns: Air density.
      :rtype: density


   .. py:property:: temperature_ratio

      Ratio of local temperature to sea-level temperature.

      :returns: **ratio** -- Temperature ratio.
      :rtype: float


   .. py:property:: density_ratio

      Ratio of local density to sea-level density.

      :returns: **ratio** -- Density ratio.
      :rtype: float


   .. py:property:: pressure_ratio

      Ratio of local pressure to sea-level pressure.

      :returns: **ratio** -- Pressure ratio.
      :rtype: float


   .. py:property:: geometric_height

      Convert geopotential altitude to geometric altitude.

      :returns: Geometric altitude.
      :rtype: height


   .. py:property:: dynamic_viscosity

      Dynamic viscosity of air.

      :returns: Dynamic viscosity.
      :rtype: viscosity


   .. py:property:: kinematic_viscosity

      Kinematic viscosity of air.

      :returns: Kinematic viscosity.
      :rtype: viscosity


   .. py:property:: speed_of_sound

      Speed of sound at the current altitude.

      :returns: Speed of sound.
      :rtype: speed


   .. py:method:: mach_number(velocity)

      Compute Mach number for a given velocity.

      :param velocity: Velocity in user-defined units.
      :type velocity: float

      :returns: **mach** -- Mach number.
      :rtype: float



   .. py:method:: dynamic_pressure(velocity)

      Compute dynamic pressure.

      :param velocity: Velocity in user-defined units.
      :type velocity: float

      :returns: Dynamic pressure.
      :rtype: pressure



   .. py:method:: __atmosphere_layer(altitude)

      Configure the appropriate atmospheric layer.



