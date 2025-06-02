# Scientific Software Development Demo

[![CI](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/ci.yml/badge.svg)](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://sfarrens.github.io/Scientific-Software-Dev-Demo/)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue.svg)](https://ghcr.io/sfarrens/scientific-software-dev-demo)

> Author: [Samuel Farrens](https://sfarrens.github.io/)  
> Email: samuel.farrens@cea.fr

This repository provides a demonstration of packaging a Python code for a course on Scientific Software Development.

The slides accompanying this repository can be found [here](https://sfarrens.github.io/presentations/#/).

Example API documentation for this repository can be found [here](https://sfarrens.github.io/Scientific-Software-Dev-Demo/).

## Changelog
- 02/06/2025: The content was updated for the [2025 COLOURS Programme](https://indico.ijclab.in2p3.fr/event/11110/)
- 26/08/2024: The content was updated for the [2024 edition of the Rodolphe Clédassou Summer School](https://ecole-euclid.cnrs.fr/2024-accueil/)
- 28/08/2023: The first version was made for the [2023 edition of the Euclid Summer School](https://ecole-euclid.cnrs.fr/2023-accueil/)

## Requirements

To follow this course you will need to have Python (ideally v3.11) installed with the following dependencies:

### Core Dependencies
- python=3.11
- numpy>=1.25
- build
- twine

### Development Dependencies
- black
- isort
- myst-parser
- numpydoc
- pytest
- pytest-emoji
- pytest-cov
- sphinx
- sphinx-book-theme

### Optional Dependencies
- astropy (for verification)

### Additional Dependencies (via pip)
- pytest-pydocstyle
- line_profiler
- memory_profiler

### Manual install

All of these packages can easily be installed from [PyPI](https://pypi.org/) using `pip`.

```bash
pip install numpy>=1.25 build twine black isort myst-parser numpydoc pytest pytest-emoji pytest-cov sphinx sphinx-book-theme pytest-pydocstyle line_profiler memory_profiler
```

### Conda install

Alternatively, you can build the [Conda](https://docs.conda.io/) environment using the `environment.yml` file provided.

```bash
conda env create -f environment.yml
```

Then you can activate the environment as follows:

```bash
conda activate mycosmo
```

### Docker image

You can run the code using the provided [Docker](https://www.docker.com/) image from the GitHub Container Registry. First, you'll need to authenticate with the GitHub Container Registry:

```bash
# Login to GitHub Container Registry
docker login ghcr.io
```

Then you can pull the latest image:

```bash
# Pull the latest image
docker pull ghcr.io/sfarrens/scientific-software-dev-demo:main
```

And run an interactive container:

```bash
# Run an interactive container with your current directory mounted
docker run --rm -it ghcr.io/sfarrens/scientific-software-dev-demo:main
```