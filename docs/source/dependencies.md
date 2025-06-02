# Dependencies

This page lists the mandatory dependencies required to use the `mycosmo` package.

## Core Dependencies

The following packages are required for basic usage of `mycosmo`:

- **Python** (>=3.11): The programming language used to develop the package
- **NumPy**: Required for numerical computations and array operations

## Installation

You can install the package and its core dependencies using pip:

```bash
pip install mycosmo
```

This will install the package and its core dependencies (NumPy).

## Optional Dependencies

While not required for basic usage, the following optional dependencies are available for specific use cases:

- **Documentation**: myst-parser, numpydoc, sphinx, sphinx-book-theme
- **Linting**: black, isort
- **Release**: build, twine
- **Testing**: pytest, pytest-cov, pytest-emoji, pytest-pydocstyle
- **Verification**: astropy
- **Development**: Includes all of the above (docs, lint, release, test)

You can install these optional dependencies using pip with the appropriate extras in development mode:

```bash
# For documentation
pip install -e "mycosmo[docs]"

# For linting
pip install -e "mycosmo[lint]"

# For release
pip install -e "mycosmo[release]"

# For profiling
pip install -e "mycosmo[profile]"

# For testing
pip install -e "mycosmo[test]"

# For verification
pip install -e "mycosmo[verify]"

# For development (includes all optional dependencies)
pip install -e "mycosmo[dev]"
```

## Version Compatibility

The package is tested and guaranteed to work with Python 3.11 or higher. While it may work with earlier versions, these are not officially supported. 