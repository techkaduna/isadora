import pytest
from isadora import ISA

# ============================================================================
# ARDC 1959 reference atmosphere (informational comparison)
# ============================================================================

ARDC_TABLE = {
    5:  {"T": 255.69, "P": 54048, "rho": 0.73643},
    16: {"T": 216.66, "P": 10353, "rho": 0.16647},
    25: {"T": 216.66, "P": 2527.3, "rho": 0.040639},
    40: {"T": 260.91, "P": 299.77,  "rho": 0.0040028},
}


@pytest.mark.parametrize("alt_km,ref", ARDC_TABLE.items())
def test_isa_vs_ardc_1959(alt_km, ref):
    """
    Compare ISA outputs against ARDC 1959 reference data.

    Notes
    -----
    This test does NOT assert strict agreement because
    ARDC uses a different stratospheric temperature model.
    """
    atm = ISA(geopotential_height=alt_km)

    print(f"\nAltitude {alt_km} km")
    print("ΔT =", atm.temperature.value - ref["T"])
    print("ΔP =", atm.pressure.value - ref["P"])
    print("Δρ =", atm.density.value - ref["rho"])
