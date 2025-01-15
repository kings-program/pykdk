from setuptools import setup, find_packages

setup(
    name="pykdk",
    version="0.1.0",
    description="Python library created by Dong-Keon Kim",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dong-Keon Kim",
    author_email="kdk199604@gmail.com",
    url="https://github.com/kings-program/pykdk",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
