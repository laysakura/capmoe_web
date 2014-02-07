#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name             = 'capmoe_web',
    description      = '''CapMoe web service''',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/capmoe_web',
    # license          = 'LICENSE.txt',
    version          = '0.0.1',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    test_suite       = 'nose.collector',
    install_requires = [
        'gunicorn',
        'Django',
        # 'rainbow_logging_handler',
    ],
    tests_require = [
        'nose',
        'coverage',
        'nose-cov',
        'nose-parameterized',
    ],
    packages = [
        'capmoe_web',
    ],
    scripts = [
    ],
    classifiers = '''
Programming Language :: Python
Development Status :: 1 - Planning
Programming Language :: Python :: 3.3
Operating System :: POSIX :: Linux
'''.strip().splitlines()
)
