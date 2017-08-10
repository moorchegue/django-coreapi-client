#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
from setuptools import setup, find_packages

__doc__ = "Django CoreAPI client"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


readme = read('README.rst')
changelog = read('CHANGELOG.rst')
version = read('VERSION').strip()

install_requires = [
    'Django>=1.11',
    'coreapi>=2.3',
]

tests_require = [
    'pytest>=3.0',
]

extras_require = {
    'testing': tests_require,
}


setup(
    name='django-coreapi-client',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + changelog,
    author='murchik',
    author_email='murchik@protonmail.com',
    url='https://github.com/vericant/django-coreapi-client',
    packages=[package for package in find_packages()],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    license="GPLv3",
    zip_safe=True,
    keywords='django-coreapi-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
