#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


tests_require = [
    'nose',
    'coverage',
    'nose-cov',
    'nose-parameterized',
    'django-nose',
],

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
    tests_require    = tests_require,
    install_requires = [
        # 'gunicorn',  # [todo] - introduce gunicorn as app server if too much load
        'Django',
        'PyMySQL',
        # 'rainbow_logging_handler',
    ],
    extras_require = {
        'testing': tests_require,
    },
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
