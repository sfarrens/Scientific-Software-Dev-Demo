# Quickstart Guide

```{warning} Demonstration Package
This is a demonstration package created for a course on Scientific Software Development. The package and its documentation are designed to showcase best practices in scientific software development. This is not a real cosmology package and should not be used in actual research.
```

This guide will help you get started with using the `mycosmo` package for cosmological calculations.

## Installation

First, install the package using pip:

```bash
pip install mycosmo
```

## Basic Usage

The package provides two main functions for cosmological calculations:

1. `hubble`: Calculate the Hubble parameter at a given redshift
2. `critical_density`: Calculate the critical density at a given redshift

### Example: Calculating the Hubble Parameter

Here's how to calculate the Hubble parameter at different redshifts:

```python
import numpy as np
from mycosmo.cosmology import hubble

# Define cosmological parameters
cosmo_dict = {
    "H0": 70,  # km/s/Mpc
    "omega_m_0": 0.3,
    "omega_k_0": 0.0,
    "omega_lambda_0": 0.7
}

# Calculate H(z) at z = 0
H0 = hubble(0.0, cosmo_dict)
print(f"H0 = {H0:.2f} km/s/Mpc")

# Calculate H(z) at multiple redshifts
z = np.array([0.5, 1.0, 2.0])
H_z = hubble(z, cosmo_dict)
for z_val, H_val in zip(z, H_z):
    print(f"H(z={z_val}) = {H_val:.2f} km/s/Mpc")
```

### Example: Calculating Critical Density

To calculate the critical density at different redshifts:

```python
from mycosmo.cosmology import critical_density

# Calculate ρ_c(z) at z = 0
rho_c0 = critical_density(0.0, cosmo_dict)
print(f"ρ_c(0) = {rho_c0:.2e} kg/m³")

# Calculate ρ_c(z) at multiple redshifts
rho_c = critical_density(z, cosmo_dict)
for z_val, rho_val in zip(z, rho_c):
    print(f"ρ_c(z={z_val}) = {rho_val:.2e} kg/m³")
```

## Cosmological Parameters

The package uses a dictionary to specify cosmological parameters. The required parameters are:

- `H0`: Hubble constant at z=0 (km/s/Mpc)
- `omega_m_0`: Matter density parameter at z=0
- `omega_k_0`: Curvature density parameter at z=0
- `omega_lambda_0`: Dark energy density parameter at z=0

## Constants

The package provides some useful cosmological constants in the `mycosmo.constants` module:

- `G`: Gravitational constant
- `Mpc`: Megaparsec in meters

You can use these constants in your calculations:

```python
from mycosmo.constants import G, Mpc

# Example: Convert H0 from km/s/Mpc to s^-1
H0_si = 70 * 1000 / Mpc  # Convert to s^-1
```

## Advanced Usage

For more advanced usage, including:

- Custom cosmological models
- Additional cosmological calculations
- Integration with other scientific packages

Please refer to the full API documentation in the {doc}`modules` section. 