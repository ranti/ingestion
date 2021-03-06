#!/usr/bin/env python

from distutils.core import setup

setup( name = 'ingestion',
       version = '0.1',
       description='DPLA Ingestion Subsystem',
       author='Mark Baker',
       author_email='mark@zepheira.com',
       url='http://dp.la',
       package_dir={'dplaingestion':'lib'},
       packages=['dplaingestion','dplaingestion.akamod'],
       scripts=['scripts/poll_profiles','scripts/build_profile'],
)
