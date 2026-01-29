isadora.base
============

.. py:module:: isadora.base

.. autoapi-nested-parse::

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

   .. rubric:: Notes

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



Attributes
----------

.. autoapisummary::

   isadora.base._is_altitude


Classes
-------

.. autoapisummary::

   isadora.base.AtmosphericLayer
   isadora.base.IsothermalLayer
   isadora.base.ISATropopause
   isadora.base.ISATroposphere
   isadora.base.ISAStratosphere
   isadora.base.ISA


Functions
---------

.. autoapisummary::

   isadora.base._choose_atmosphere


Module Contents
---------------

.. py:data:: _is_altitude

.. py:class:: AtmosphericLayer

   Abstract base class for ISA atmospheric layers.

   Each atmospheric layer must implement temperature and pressure
   as functions of altitude.

   .. attribute:: lapse_rate

      Temperature lapse rate of the layer.

      :type: float

   .. rubric:: Notes

   This class should not be instantiated directly.


   .. py:attribute:: lapse_rate
      :type:  float
      :value: 0.0



   .. py:property:: temperature
      :abstractmethod:


      Temperature at the current altitude.

      :returns: Temperature corresponding to the altitude within the layer.
      :rtype: temperature


   .. py:property:: pressure
      :abstractmethod:


      Pressure at the current altitude.

      :returns: Pressure corresponding to the altitude within the layer.
      :rtype: pressure


.. py:class:: IsothermalLayer(parent)

   Bases: :py:obj:`AtmosphericLayer`


   Base class for ISA isothermal atmospheric layers.

   In an isothermal layer, temperature does not vary with altitude.

   :param parent: Parent ISA instance providing altitude and unit context.
   :type parent: ISA

   .. attribute:: lapse_rate

      Temperature lapse rate (zero for isothermal layers).

      :type: float

   .. attribute:: parent

      Reference to the owning ISA instance.

      :type: ISA


   .. py:attribute:: lapse_rate
      :type:  float
      :value: 0.0



   .. py:attribute:: parent


   .. py:property:: temperature

      Temperature within the isothermal layer.

      :returns: Constant temperature value.
      :rtype: temperature


   .. py:property:: temperature_ratio

      Ratio of layer temperature to sea-level temperature.

      :returns: **ratio** -- Temperature ratio.
      :rtype: float


   .. py:property:: pressure

      Pressure within the isothermal layer.

      :returns: Pressure corresponding to altitude.
      :rtype: pressure


.. py:class:: ISATropopause(parent)

   Bases: :py:obj:`AtmosphericLayer`


   ISA tropopause atmospheric layer (11 km – 25 km).

   The tropopause is an isothermal layer where temperature
   remains constant with altitude.

   :param parent: Parent ISA instance.
   :type parent: ISA

   .. attribute:: base_temperature

      Temperature at the base of the tropopause.

   .. attribute:: base_pressure

      Pressure at the base of the tropopause.

   .. attribute:: base_density

      Density at the base of the tropopause.

   .. attribute:: base_height

      Base altitude of the tropopause layer.


   .. py:attribute:: base_temperature


   .. py:attribute:: base_pressure


   .. py:attribute:: base_density


   .. py:attribute:: base_height


   .. py:attribute:: parent


   .. py:method:: __repr__()


   .. py:property:: temperature

      Temperature within the tropopause layer.

      :returns: Temperature at the specified altitude.
      :rtype: temperature


   .. py:property:: __exp_num

      Internal exponential term for pressure computation.

      :returns: **value** -- Exponential coefficient.
      :rtype: float


   .. py:property:: pressure

      Pressure within the tropopause layer.

      :returns: Pressure at the specified altitude.
      :rtype: pressure


.. py:class:: ISATroposphere(parent)

   Bases: :py:obj:`AtmosphericLayer`


   ISA troposphere atmospheric layer (0 km – 11 km).

   The troposphere exhibits a negative temperature lapse rate.

   :param parent: Parent ISA instance.
   :type parent: ISA


   .. py:attribute:: lapse_rate


   .. py:attribute:: parent


   .. py:attribute:: base_temperature
      :value: 288.15



   .. py:method:: __repr__()


   .. py:property:: temperature

      Temperature within the troposphere.

      :returns: Temperature at the specified altitude.
      :rtype: temperature


   .. py:property:: __temperature_ratio

      Internal temperature ratio helper.

      :returns: **ratio** -- Temperature ratio relative to sea level.
      :rtype: float


   .. py:property:: pressure

      Pressure within the troposphere.

      :returns: Pressure at the specified altitude.
      :rtype: pressure


.. py:class:: ISAStratosphere(parent)

   Bases: :py:obj:`AtmosphericLayer`


   ISA stratosphere atmospheric layer (20 km – 47 km).

   The stratosphere is divided into lower and upper regions,
   each with different lapse rates.

   :param parent: Parent ISA instance.
   :type parent: ISA


   .. py:attribute:: lapse_rate


   .. py:attribute:: base_temp


   .. py:attribute:: base_pressure


   .. py:attribute:: __is_lower_strat
      :value: True



   .. py:attribute:: parent


   .. py:method:: __repr__()


   .. py:property:: temperature

      Temperature within the stratosphere.

      :returns: Temperature at the specified altitude.
      :rtype: temperature


   .. py:property:: pressure

      Pressure within the stratosphere.

      :returns: Pressure at the specified altitude.
      :rtype: pressure


.. py:function:: _choose_atmosphere(altitude)

   Select the appropriate ISA atmospheric layer.

   :param altitude: Geopotential altitude in kilometers (SI).

   :returns: **layer** -- Atmospheric layer class.
   :rtype: AtmosphericLayer

   :raises Exception: If altitude exceeds stratospheric limits.


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



