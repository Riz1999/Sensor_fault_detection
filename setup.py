from setuptools import find_packages,setup

setup(
    name='py_test',
    version='0.0.1',
    author="rizwan",
    author_email="rizwanzhad@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo[srv]==4.2.0"],
)    