# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-simpleblog',
    packages=find_packages(),
    version='0.3',
    description='Simple blog application for django framework',
    author='Commite',
    author_email='hola@commite.co',
    url='https://github.com/commite/simpleblog',
    keywords=['django', 'blog'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8"
    ],
)
