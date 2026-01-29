test_isadora
============

.. py:module:: test_isadora

.. autoapi-nested-parse::

   test_isadora.py

   Comprehensive test suite for Isadora (ICAO 1983 ISA implementation).
   Tests atmospheric properties, unit conversions, derived quantities, and constants.



Attributes
----------

.. autoapisummary::

   test_isadora.ICAO_REFERENCE


Functions
---------

.. autoapisummary::

   test_isadora.test_isa_properties_against_icao
   test_isadora.test_mach_number_calculation
   test_isadora.test_dynamic_pressure
   test_isadora.test_geometric_height_conversion
   test_isadora.test_to_user_unit_conversion
   test_isadora.test_constants_immutability
   test_isadora.test_constants_values
   test_isadora.test_layer_boundaries


Module Contents
---------------

.. py:data:: ICAO_REFERENCE

.. py:function:: test_isa_properties_against_icao(altitude, ref)

.. py:function:: test_mach_number_calculation()

.. py:function:: test_dynamic_pressure()

.. py:function:: test_geometric_height_conversion()

.. py:function:: test_to_user_unit_conversion()

.. py:function:: test_constants_immutability()

.. py:function:: test_constants_values()

.. py:function:: test_layer_boundaries()

