#!/usr/bin/env python

from setuptools import setup
import sys

if sys.version_info[0] == 2:
    from commands import getoutput
    requires = []
elif sys.version_info[0] == 3:
    from subprocess import getoutput
    requires = ['urllib3']


version = getoutput('git describe --always') or '1.0'
if not version.startswith('1.'):
    print('Failed to get version from git: %s' % version)
    sys.exit(1)


setup(name='unifi',
      version=version,
      description='API towards Ubiquity Networks UniFi controller',
      author='Jakob Borg',
      author_email='jakob@nym.se',
      url='https://github.com/calmh/unifi-api',
      packages=['unifi'],
      requires=requires,
      scripts=['unifi-low-snr-reconnect', 'unifi-ls-clients',
               'unifi-save-statistics', 'unifi-log-roaming'],
      classifiers=['Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Networking']
     )
