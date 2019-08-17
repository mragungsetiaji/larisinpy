from setuptools import setup

# Package details
setup(
    name="larisin",
    version="1.0.0",
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
        "pandas"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
