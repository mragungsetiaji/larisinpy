from setuptools import setup

# Package details
setup(
    name="larisin",
    version="0.0.2",
    entry_points={
        "console_scripts": ["larisin = larisin.cli:main"]
    },
    author="Agung Setiaji",
    author_email="mragungsetiaji@gmail.com",
    url="https://github.com/mragungsetiaji/larisinpy",
    description="Larisin CLI",
    license="BSD 3-Clause License",
    packages=[
        "larisin"
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
