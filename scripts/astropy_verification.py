"""ASTROPY VERIFICATION.

This script compares the performance of `mycosmo` to routines provided in Astropy.

"""

import numpy as np
from astropy.cosmology import WMAP9 as cosmo

from mycosmo.cosmology import critical_density, hubble


class TestAstropy:
    """Test Astropy.

    Class to test ``mycosmo`` routines with respect to those provided in Astropy.

    """

    redshift = np.array([0.0, 0.5, 1.0])
    cosmo_dict = {
        "H0": cosmo.H0.value,
        "omega_m_0": cosmo.Om0,
        "omega_k_0": cosmo.Ok0,
        "omega_lambda_0": cosmo.Ode0,
    }

    def test_hubble(cls):
        """Test Hubble function."""
        h_mycosmo = hubble(redshift=cls.redshift, cosmo_dict=cls.cosmo_dict)
        h_astropy = cosmo.H(cls.redshift).value

        assert (abs(h_mycosmo - h_astropy) < 0.1).all()

    def test_critical_density(cls):
        """Test Critical Density function."""
        rho_crit_mycosmo = (
            critical_density(redshift=cls.redshift, cosmo_dict=cls.cosmo_dict) * 1e26
        )
        rho_crit_astropy = cosmo.critical_density(cls.redshift).value * 1e29

        assert (abs(rho_crit_mycosmo - rho_crit_astropy) < 0.01).all()


def main():
    """Run main script function."""
    TestAstropy().test_hubble()
    TestAstropy().test_critical_density()


if __name__ == "__main__":
    exit(main())
