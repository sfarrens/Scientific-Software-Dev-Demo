import numpy as np

from .constants import Mpc, G


def hubble(redshift, cosmo_dict):
    r"""Hubble Parameter.

    Calculate the Hubble parameter at a given redshift.

    Parameters
    ----------
    redshift : float
        Redshift
    cosmo_dict : dict
        Dictionary of cosmological constants

    Returns
    -------
    float
        Value of the Hubble parameter

    Notes
    -----
    Implements

    .. math::
        H(z) = \sqrt{H_0^2 \Omega_{m,0}(1+z)^3 + \Omega_{Lambda,0} +
            \Omega_{K,0}(1+z)^2}

    """
    hubble_const = cosmo_dict["H0"]
    matter = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    curvature = cosmo_dict["omega_k_0"] * (1 + redshift) ** 2
    dark_energy = cosmo_dict["omega_lambda_0"]

    return np.sqrt(hubble_const**2 * (matter + curvature + dark_energy))


def critical_density(redshift, cosmo_dict):
    r"""Critical Density.

    Calculate the critical density at a given redshift.

    Parameters
    ----------
    redshift : float
        Redshift
    cosmo_dict : dict
        Dictionary of cosmological constants

    Returns
    -------
    float
        Value of the critical density

    Notes
    -----
    Implements

    .. math::

        \rho_c(z) = \frac{3H^2(z)}{8\pi G}

    """
    H_z_si = hubble(redshift, cosmo_dict) * 1e3 / Mpc

    return (3.0 * H_z_si**2) / (8.0 * np.pi * G)
