# -*- coding: utf-8 -*-
"""
Created on 2021/11/8 8:15 下午
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""

from os.path import dirname, join

import setuptools

with open(join(dirname(__file__), "VERSION"), "rb") as f:
    version = f.read().decode("ascii").strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()

requires = []

setuptools.setup(
    name="feapson",
    version=version,
    author="Boris",
    license="MIT",
    author_email="boris_liu@foxmail.com",
    python_requires=">=3",
    description="Same as json.dumps or json.loads, feapson supprot feapson.dumps and feapson.loads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
    url="https://github.com/Boris-code/feapson.git",
    packages=packages,
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
)
