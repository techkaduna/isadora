isadora.units
=============

.. py:module:: isadora.units

.. autoapi-nested-parse::

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

   .. rubric:: Notes

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

   .. attribute:: si_units

      

   .. attribute:: uscs_units

      

   .. attribute:: imperial_units

      

   .. attribute:: si

      

   .. attribute:: uscs

      

   .. attribute:: imperial

      



Attributes
----------

.. autoapisummary::

   isadora.units.KELVIN_PER_METER
   isadora.units.FARENHEIT_PER_FEET
   isadora.units.CELSIUS_PER_FEET
   isadora.units.KILOGRAM_PER_METER_SECOND
   isadora.units.SLUG_PER_FEET_SECOND
   isadora.units.POUND_PER_FEET_SECOND
   isadora.units.METER_SQR_PER_SECOND
   isadora.units.FEET_PER_SQR_SECOND
   isadora.units.JOULE_PER_KILOGRAM_KELVIN
   isadora.units.JOULE_PER_MOL_KELVIN
   isadora.units.KILOGRAM_PER_MOL
   isadora.units._make_unit
   isadora.units.si_units
   isadora.units.uscs_units
   isadora.units.imperial_units
   isadora.units.si
   isadora.units.uscs
   isadora.units.imperial
   isadora.units._set_SI_standard


Classes
-------

.. autoapisummary::

   isadora.units.QuantityTable
   isadora.units.UnitRegistry
   isadora.units._UnitParam


Functions
---------

.. autoapisummary::

   isadora.units.to_si
   isadora.units.to_user_unit


Module Contents
---------------

.. py:class:: QuantityTable

   Container mapping physical quantities to unit constructors.

   This dataclass groups callable constructors for each physical
   quantity under a given unit standard (SI, USCS, Imperial).

   .. attribute:: UNIT_NAME

      Name of the unit system.

      :type: str

   .. attribute:: TEMPERATURE

      Temperature unit constructor.

      :type: Callable

   .. attribute:: DENSITY

      Density unit constructor.

      :type: Callable

   .. attribute:: PRESSURE

      Pressure unit constructor.

      :type: Callable

   .. attribute:: DISTANCE

      Length / distance unit constructor.

      :type: Callable

   .. attribute:: DYNAMIC_VISCOSITY

      Dynamic viscosity unit constructor.

      :type: Callable

   .. attribute:: KINEMATIC_VISCOSITY

      Kinematic viscosity unit constructor.

      :type: Callable

   .. attribute:: SPEED

      Speed unit constructor.

      :type: Callable

   .. attribute:: LAPSE_RATE

      Temperature lapse-rate unit constructor.

      :type: Callable

   .. attribute:: UNIV_GAS_CONSTANT

      Universal gas constant unit constructor.

      :type: Callable

   .. attribute:: EARTH_MOLAR_MASS

      Earth molar mass unit constructor.

      :type: Callable

   .. attribute:: SPEC_HEAT_CONSTANT

      Specific heat constant unit constructor.

      :type: Callable


   .. py:attribute:: UNIT_NAME
      :type:  str


   .. py:attribute:: TEMPERATURE
      :type:  Callable


   .. py:attribute:: DENSITY
      :type:  Callable


   .. py:attribute:: PRESSURE
      :type:  Callable


   .. py:attribute:: DISTANCE
      :type:  Callable


   .. py:attribute:: DYNAMIC_VISCOSITY
      :type:  Callable


   .. py:attribute:: KINEMATIC_VISCOSITY
      :type:  Callable


   .. py:attribute:: SPEED
      :type:  Callable


   .. py:attribute:: LAPSE_RATE
      :type:  Callable


   .. py:attribute:: UNIV_GAS_CONSTANT
      :type:  Callable


   .. py:attribute:: EARTH_MOLAR_MASS
      :type:  Callable


   .. py:attribute:: SPEC_HEAT_CONSTANT
      :type:  Callable


.. py:data:: KELVIN_PER_METER

.. py:data:: FARENHEIT_PER_FEET

.. py:data:: CELSIUS_PER_FEET

.. py:data:: KILOGRAM_PER_METER_SECOND

.. py:data:: SLUG_PER_FEET_SECOND

.. py:data:: POUND_PER_FEET_SECOND

.. py:data:: METER_SQR_PER_SECOND

.. py:data:: FEET_PER_SQR_SECOND

.. py:data:: JOULE_PER_KILOGRAM_KELVIN

.. py:data:: JOULE_PER_MOL_KELVIN

.. py:data:: KILOGRAM_PER_MOL

.. py:data:: _make_unit

   Internal helper to construct GenericUnit2 callables.

.. py:data:: si_units

.. py:data:: uscs_units

.. py:data:: imperial_units

.. py:data:: si

.. py:data:: uscs

.. py:data:: imperial

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



.. py:data:: _set_SI_standard

   Internal helper to construct SI-unit quantities.

.. py:class:: _UnitParam(name: str, quantity: str)

   Descriptor for immutable, unit-aware parameters.

   This descriptor allows attributes to be assigned once and
   automatically converted to SI units.

   :param name: Attribute name.
   :type name: str
   :param quantity: Physical quantity type.
   :type quantity: str


   .. py:attribute:: name


   .. py:attribute:: quantity


   .. py:method:: __get__(instance, cls)


   .. py:method:: __set__(instance, value)


.. py:function:: to_si(x: float, quantity: str)

   Convert a value from the active unit system to SI.

   :param x: Value in user-defined units.
   :type x: float
   :param quantity: Physical quantity name.
   :type quantity: str

   :returns: Value converted to SI units.
   :rtype: value


.. py:function:: to_user_unit(x, quantity: str)

   Convert a value from SI units to the active user unit system.

   :param x: Value assumed to be in SI units.
   :type x: float
   :param quantity: Physical quantity name.
   :type quantity: str

   :returns: Value converted to the active user unit system.
   :rtype: value


