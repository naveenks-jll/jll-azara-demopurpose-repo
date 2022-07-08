#!/usr/bin/env python

"""The setup script."""
import os
import re
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

def get_version():
    init = open(os.path.join(ROOT, 'demopurposepkg', '_version.py')).read()
    return VERSION_RE.search(init).group(1)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Naveen Ks",
    author_email='naveen.ks@jll.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Azara V2 Python Template.",
    entry_points={
        'console_scripts': [
            'demopurposepkg=demopurposepkg.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='demopurposepkg',
    name='demopurposepkg',
    packages=find_packages(include=['demopurposepkg', 'demopurposepkg.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/naveenks-jll/demopurposepkg',
    version=get_version(),
    zip_safe=False,
)
