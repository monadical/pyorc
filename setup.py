#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="pyorc",
    description="pyorc is a front and backend to control river camera observation locations",
    version="0.1.0.dev",
    long_description=readme + "\n\n",
    long_description_content_type="text/markdown",
    url="https://github.com/localdevices/pyorc",
    author="Hessel Winsemius",
    author_email="winsemius@rainbowsensing.com",
    packages=find_packages(),
    package_dir={"pyorc": "pyorc"},
    test_suite="tests",
    python_requires=">=3.8",
    install_requires=[
        "cython; platform_machine != 'x86_64'",
        "dask",
        "descartes",
        "geojson",
        "matplotlib",
        "netCDF4",
        "numpy",
        "opencv-python-headless",
        "openpiv",
        "packaging; platform_machine != 'x86_64'",
        "pip",
        "pyproj",
        "pythran; platform_machine != 'x86_64'",
        "rasterio",
        "scikit-image",
        "scipy",
        "shapely",
        "tqdm",
        "xarray",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
        "optional": [],
    },
    # entry_points="""
    # """,
    include_package_data=True,
    license="GPLv3",
    zip_safe=False,
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Scientific/Engineering :: Image Processing",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="hydrology hydrometry river-flow pyorc",
)
