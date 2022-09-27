#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.classes.classes import bcolors
from pywarden.logger import logger
import os

def check_bw_cli():
    if os.system('command -v bw &>> /dev/null') != 0:
        logger.pywarden_logger(Payload="Bitwarden CLI not found", Color="red", ErrorExit=True, Exit=False)
