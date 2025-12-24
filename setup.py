"""Prefect Framework Library.

A flexible Prefect orchestration library with registry pattern for managing flows and tasks.
"""

from setuptools import setup, find_packages

setup(
    name="prefect-framework",
    version="1.0.0",
    author="Grepx Team",
    author_email="support@grepx.com",
    description="A flexible Prefect orchestration library with registry pattern",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/grepx-support/prefect-framework",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "prefect>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
    },
)