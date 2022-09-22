#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.pywarden import handle_config
import os

def pywarden_version():
    dir = handle_config.get_dir()
    # Check if file pyproject.toml exists
    if os.path.isfile(dir + '/' + 'pyproject.toml'):
        # Read the file
        with open(dir + '/' + 'pyproject.toml', 'r') as file:
            pyproject_toml = file.read()
        # Get the version number
        pywarden_version = pyproject_toml.split('version = "')[1].split('"')[0]
        return pywarden_version
