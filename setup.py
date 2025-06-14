"""
Setup script for Hindi Transliteration Library
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="hindi_xlit",
    version="1.0.0",
    author="Aman Ranjan Verma",
    author_email="your.email@example.com",  # Update this
    description="A Hindi transliteration package using AI4Bharat's model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hindi_xlit",  # Update this
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "hindi-xlit=hindi_xlit.interactive_transliterate:main",
        ],
    },
    include_package_data=True,
    package_data={
        "hindi_xlit": ["models/hindi/*"],
    },
) 