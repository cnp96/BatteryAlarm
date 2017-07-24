# setup.py
from distutils.core import setup
import py2exe

setup(windows=["BatteryAlert.py"],
      options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
      zipfile=None,)
