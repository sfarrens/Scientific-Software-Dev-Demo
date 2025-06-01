# Scientific Software Development Demo
> Author: [Samuel Farrens](https://sfarrens.github.io/)  
> Email: samuel.farrens@cea.fr

This repository provides a demonstration of packaging a Python code for a course on Scientific Software Development.

The slides accompanying this repository can be found [here](https://sfarrens.github.io/presentations/#/).

Example API documentation for this repository can be found [here](https://sfarrens.github.io/ecole-euclid-2023/).

## Changelog
- 01/06/2025: The content was updated for the [2025 COLOURS Programme](https://indico.ijclab.in2p3.fr/event/11110/)
- 26/08/2024: The content was updated for the [2024 edition of the Rodolphe Clédassou Summer School](https://ecole-euclid.cnrs.fr/2024-accueil/)
- 28/08/2023: The first version was made for the [2023 edition of the Euclid Summer School](https://ecole-euclid.cnrs.fr/2023-accueil/)

## Requirements

To follow this course you will need to have Python (ideally v3.11) installed with the following dependencies:

- numpy
- astropy
- black
- isort
- myst-parser
- numpydoc
- pytest
- pytest-pydocstyle
- pytest-emoji
- pytest-cov
- sphinx
- sphinx-book-theme
- twine

### Manual install

All of these packages can easily be installed from [PyPI](https://pypi.org/) using `pip`.

```bash
pip install numpy black ...
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

Finally, you can avoid installing any of the packages by simply pulling the provided [Docker](https://www.docker.com/) image. Note that you will need to [log in to the GitHub container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

```bash
docker login ghcr.io ...
docker pull ghcr.io/sfarrens/Scientific-Software-Dev-Demo:main
docker tag ghcr.io/sfarrens/Scientific-Software-Dev-Demo:main mycosmo
```

Then you can launch an interactive container as follows:

```bash
docker run --rm -itv $PWD:/home mycosmo
```
