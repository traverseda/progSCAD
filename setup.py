#!/usr/bin/env python
from distutils.core import setup
import versioneer

setup(name='progSCAD',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='progSCAD is programming tools for openSCAD. This repo includes test cases, documentation, and of course the actual ".scad" files.',
      author='Alex Davies',
      author_email='traverse.da@gmail.com',
      packages=[],
     )
