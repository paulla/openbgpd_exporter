#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Simon RECHER",
    author_email='github@recher.fr',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Exporter Prometheus for OpenBGP ",
    entry_points={
        'console_scripts': [
            'openbgpd_exporter=openbgpd_exporter.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='openbgpd_exporter',
    name='openbgpd_exporter',
    packages=find_packages(include=['openbgpd_exporter', 'openbgpd_exporter.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/voileux/openbgpd_exporter',
    version='0.1.0',
    zip_safe=False,
)
