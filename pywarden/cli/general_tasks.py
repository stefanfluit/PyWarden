#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.classes.classes import bcolors
import os

def check_bw_cli():
    if os.system('command -v bw &>> /dev/null') != 0:
        print(f"{bcolors.WARNING}Warning, BW not found!{bcolors.ENDC}")
        exit()
