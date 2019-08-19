from setuptools import setup

# Package details
setup(
    name="larisinpy",
    version="0.0.12",
    author="Agung Setiaji",
    author_email="mragungsetiaji@gmail.com",
    url="https://github.com/mragungsetiaji/larisinpy",
    description="Larisinpy",
    license="BSD 3-Clause License",
    packages=[
        "larisinpy",
        "larisinpy.connection"
    ],
    install_requires=[
        "firebase-admin"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6"
    ]
)
