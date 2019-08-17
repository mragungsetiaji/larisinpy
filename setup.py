from setuptools import setup

# Package details
setup(
    name="larisinpy",
    version="0.0.2",
    entry_points={
        "console_scripts": ["larisinpy = larisinpy.cli:main"]
    },
    author="Agung Setiaji",
    author_email="mragungsetiaji@gmail.com",
    url="https://github.com/mragungsetiaji/larisinpy",
    description="Larisinpy CLI",
    license="BSD 3-Clause License",
    packages=[
        "larisinpy"
    ],
    install_requires=[
        "pandas",
        "dask",
        "firebase-admin"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6"
    ]
)
