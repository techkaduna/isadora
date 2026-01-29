isadora.constants
=================

.. py:module:: isadora.constants

.. autoapi-nested-parse::

   isadora.constants
   =================

   Physical and atmospheric constants used throughout the ISADORA package.

   This module defines a centralized container for physical constants
   required by the International Standard Atmosphere (ISA) model and
   related thermodynamic computations. All constants are expressed in
   SI units and wrapped using the internal unit-handling system.

   The constants are instantiated once and exposed through the
   :data:`CONSTANTS` object.

   .. rubric:: Notes

   - Constants are stored as unit-aware objects where applicable.
   - Values correspond to standard ISA sea-level conditions unless
     otherwise stated.
   - This module is intended to be read-only after initialization.

   Classes
   -------
   __Constants

   .. attribute:: CONSTANTS

      Singleton instance containing all defined constants.

      :type: __Constants



Attributes
----------

.. autoapisummary::

   isadora.constants.CONSTANTS


Classes
-------

.. autoapisummary::

   isadora.constants.__Constants


Module Contents
---------------

.. py:class:: __Constants

   Container class for physical and atmospheric constants.

   This class encapsulates all constants used by the ISA model,
   including sea-level reference values and universal physical
   constants. Each constant is defined as a unit-aware parameter
   and initialized with its corresponding numerical value.

   .. rubric:: Notes

   This class is intended for internal use only and should not be
   instantiated directly by users. A singleton instance is exposed
   as :data:`CONSTANTS`.


   .. py:attribute:: MSL_TEMPERATURE
      :type:  isadora.units._UnitParam


   .. py:attribute:: MSL_PRESSURE
      :type:  isadora.units._UnitParam


   .. py:attribute:: MSL_DENSITY
      :type:  isadora.units._UnitParam


   .. py:attribute:: MSL_DYNAMIC_VISCOSITY
      :type:  isadora.units._UnitParam


   .. py:attribute:: MSL_KINEMATIC_VISCOSITY
      :type:  isadora.units._UnitParam


   .. py:attribute:: g
      :type:  isadora.units._UnitParam


   .. py:attribute:: R
      :type:  isadora.units._UnitParam


   .. py:attribute:: R_
      :type:  isadora.units._UnitParam


   .. py:attribute:: r
      :type:  isadora.units._UnitParam


   .. py:attribute:: M
      :type:  isadora.units._UnitParam


   .. py:attribute:: a_o
      :type:  isadora.units._UnitParam


   .. py:attribute:: y
      :type:  float | int
      :value: 1.4



   .. py:attribute:: c_p
      :type:  isadora.units._UnitParam


   .. py:attribute:: c_v
      :type:  isadora.units._UnitParam


   .. py:attribute:: S
      :type:  isadora.units._UnitParam


.. py:data:: CONSTANTS

   Singleton instance containing all physical and atmospheric constants.

   This object should be imported and used wherever constants are
   required within the ISADORA package.

