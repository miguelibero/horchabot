#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf8') as f:
    license = f.read()

setup(
    name='horchabot',
    version='1.0.0',
    description='web app to detect if there is horchata in the office',
    long_description=readme,
    author='Miguel Ibero',
    author_email='miguel@ibero.me',
    url='http://github.com/miguelibero/horchabot',
    license=license,
    python_requires='>=3.6.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask>~1.1.1',
    ],
    extras_require={
        "test":[
            "pytest",
            "coverage"
        ]
    }
)