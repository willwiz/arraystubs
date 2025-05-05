"""
Module to expose more detailed version info for the installed `numpy`
"""

version = "0.0.1"
__version__ = version
full_version = version

release = "dev" not in version and "+" not in version
short_version = version.split("+")[0]
