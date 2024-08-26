import numpy as np
import numpy.testing as npt

from mycosmo.cosmology import critical_density, hubble


class TestCosmology:
    fid_cosmo = {
        "H0": 70,
        "omega_m_0": 0.3,
        "omega_k_0": 0.0,
        "omega_lambda_0": 0.7,
    }
    H_tolerance = 0.01
    rho_crit_tolerance = 0.01
    z_range = np.array([0.0, 0.5, 1.0])
    H_expect = np.array([70, 91.60, 123.24])
    rho_crit_expect = np.array([09.0, 1.51, 2.7]) * 1e-26

    def test_hubble(self):
        H_vals = hubble(self.z_range, self.fid_cosmo)

        npt.assert_allclose(
            H_vals,
            self.H_expect,
            atol=self.H_tolerance,
            err_msg=(
                "The H(z) differs from expected values by more than "
                f"{self.H_tolerance} decimal places."
            ),
        )

    def test_critical_density(self):
        rho_crit_vals = critical_density(self.z_range, self.fid_cosmo)

        npt.assert_allclose(
            rho_crit_vals,
            self.rho_crit_expect,
            atol=self.rho_crit_tolerance,
            err_msg=(
                "The rho_crit(z) differs from expected values by more "
                f"than {self.rho_crit_tolerance} decimal places."
            ),
        )
