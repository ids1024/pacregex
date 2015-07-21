#!/usr/bin/env python3

from distutils.core import setup

setup(name='pacregex',
      version='0.1',
      description='Advanced regex search of pacman repositories.',
      author='Ian D. Scott',
      author_email='ian@perebruin.com',
      license = "GPL3",
      url='http://github.com/ids1024/pacregex/',
      data_files=[
          ('/usr/share/man/man1', ['pacregex.1']),
          ],
      scripts = ['pacregex'],
     )
