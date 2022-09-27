#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
import os

from pywarden.logger import logger
from pywarden.pywarden import handle_config

def bw_unlock():
    child = pexpect.spawn('bw', ['unlock', '--raw'], encoding='utf-8')
    child.expect('password')
    child.sendline(handle_config.BITWARDEN_MASTER_PASSWORD)
    child.expect(pexpect.EOF)
    if 'Invalid master password.' in child.before:
        logger.pywarden_logger(Payload="Invalid master password.", Color="red", ErrorExit=True, Exit=False)
    global BITWARDEN_SESSION_KEY
    BITWARDEN_SESSION_KEY = child.before.splitlines()[-1]
    os.environ['BW_SESSION'] = str(BITWARDEN_SESSION_KEY)
    return BITWARDEN_SESSION_KEY
