# École Euclid 2023
> Author: [Samuel Farrens](https://sfarrens.github.io/)  
> Email: samuel.farrens@cea.fr

This repository was made for a course on scientific software development at the [2023 edition of the Euclid Summer School](https://ecole-euclid.cnrs.fr/2023-accueil/).

The slides accompanying this repository can be found [here](https://sfarrens.github.io/presentations/#/).

## Requirements

To follow this course you will need to have Python (ideally v3.11) installed with the following dependencies:

- numpy
- black
- myst-parser
- numpydoc
- pytest
- pytest-black
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

Finally, you can avoid installing any of the packages by simply pulling the provided [Docker](https://www.docker.com/) image.

```bash
docker pull ghcr.io/sfarrens/ecole-euclid-2023:main
docker tag ghcr.io/sfarrens/ecole-euclid-2023:main ecole-euclid-2023
```

Then you can launch an interactive container as follows:

```bash
docker run -it ecole-euclid-2023
conda activate mycosmo
```