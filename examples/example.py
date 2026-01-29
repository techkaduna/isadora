"""
example.py

A comprehensive tutorial demonstrating:
- Computation of ISA 1983 atmospheric properties at selected altitudes
- Derived quantities: dynamic pressure, Mach number, geometric height
- Temperature offset handling
- Proper plotting of atmospheric profiles up to 20 km
"""

import os, sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isadora import ISA
from isadora.units import UnitRegistry

# -------------------------------
# Set preferred unit system
# -------------------------------
UnitRegistry.set_unit_standard("SI")  # Options: "SI", "USCS", "IMPERIAL"

# -------------------------------
# Selected altitudes for demonstration
# -------------------------------
altitudes = [0.0, 5.0, 10.0, 15.0, 20.0]  # km
isa_objects = [ISA(geopotential_height=h) for h in altitudes]

# -------------------------------
# Display ISA properties at selected altitudes
# -------------------------------
print("\n=== ISA Properties at Selected Altitudes ===")
for isa in isa_objects:
    h = isa.altitude
    print(f"\n--- Geopotential Height: {h} ---")
    print(f"Temperature: {isa.temperature}")
    print(f"Pressure: {isa.pressure}")
    print(f"Density: {isa.density}")
    print(f"Dynamic viscosity: {isa.dynamic_viscosity}")
    print(f"Kinematic viscosity: {isa.kinematic_viscosity}")
    print(f"Speed of sound: {isa.speed_of_sound}")
    print(f"Atmospheric layer: {isa.atmosphere}")

# -------------------------------
# Aircraft flight properties at 250 m/s at 10 km
# -------------------------------
velocity = 250.0  # m/s
atm_10km = ISA(geopotential_height=10.0)
q = atm_10km.dynamic_pressure(velocity)
M = atm_10km.mach_number(velocity)
print("\n=== Aircraft Flight Properties at 10 km (250 m/s) ===")
print(f"Dynamic pressure: {q}")
print(f"Mach number: {M:.2f}")

# -------------------------------
# Temperature offset example (+5 K)
# -------------------------------
isa_offset = ISA(geopotential_height=10.0, offset=5.0)
print("\n=== Temperature Offset Example (+5 K) ===")
print(f"Temperature at 10 km with offset: {isa_offset.temperature} K")
print(f"Layer with offset: {isa_offset.atmosphere}")

# -------------------------------
# Corrected plotting of ISA profiles up to 20 km
# -------------------------------
h_profile = np.linspace(0, 20, 201)  # 0 to 20 km in 0.1 km steps
T_profile = []
P_profile = []
rho_profile = []

for h in h_profile:
    isa_h = ISA(geopotential_height=h)
    T_profile.append(isa_h.temperature.value)
    P_profile.append(isa_h.pressure.value)
    rho_profile.append(isa_h.density.value)

plt.figure(figsize=(10, 6))

# Plot Temperature (linear)
plt.plot(T_profile, h_profile, label="Temperature (K)", color="red", linewidth=2)
# Plot Density (linear)
plt.plot(rho_profile, h_profile, label="Density (kg/m³)", color="green", linewidth=2)
# Plot Pressure (log scale for better visibility)
plt.plot(P_profile, h_profile, label="Pressure (Pa)", color="blue", linewidth=2)
plt.xscale("log")

# Invert y-axis so sea level is at bottom
plt.gca().invert_yaxis()

plt.xlabel("Value")
plt.ylabel("Geopotential Height (km)")
plt.title("ISA 1983 Atmospheric Profiles up to 20 km")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
